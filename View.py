#!/usr/bin/env python
# Written by: DGC

import sys
# renamed module in python 3
if (sys.version_info[:2] < (3,0)):
    from Tkinter import *
else:
    from tkinter import *

import MVVM

#==============================================================================
class TKinterView(MVVM.View):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    def __init__(self, parent, context):
        # intialise as a mvvm view then set up the data context, parent window
        super(TKinterView, self ).__init__()

        self.context = context
        self.parent = parent

        self.style = "DGC"

        self.window = Toplevel(self.parent)
        self.window.title("MVVM Email Sender")

        # hook up the delete button so that it quits the window and doesn't 
        # make the main program hang
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)
        self.apply_style(self.window)

        self.center_window(self.window, 600, 460)
        self.border = Frame(self.window, relief="flat", borderwidth=20)

        self.server_label = Label(self.window, text = "Server")
        self.apply_style(self.server_label)
        self.server_label.grid(row = 0, column = 0, sticky = W)

        self.server_text_box = Entry(self.window)
        self.server_text_box.grid(row = 0, column = 1)
        self.bind_data(self.server_text_box, "server")

        self.recipient_label = Label(self.window)
        self.apply_style(self.recipient_label)
        self.recipient_label.grid(row = 1, column = 0, sticky = W)
        self.bind_data(self.recipient_label, "recipient_label")

        self.recipient_text_box = Entry(self.window)
        self.recipient_text_box.grid(row = 1, column = 1)
        self.bind_data(self.recipient_text_box,  "recipient")

        self.sender_label = Label(self.window, text = "From")
        self.apply_style(self.sender_label)
        self.sender_label.grid(row = 2, column = 0, sticky = W)

        self.sender_text_box = Entry(self.window)
        self.sender_text_box.grid(row = 2, column = 1)
        self.bind_data(self.sender_text_box, "email")

        self.authenticate_button = Checkbutton(
            self.window,
            text="Authenticate?",
            command = self.show_hide_authentication
            )
        self.bind_data(self.authenticate_button, "authentification")
        self.apply_style(self.authenticate_button)
        self.authenticate_button.grid(row = 2, column = 2, columnspan = 2)

        self.username_label = Label(
            self.window,
            text = "Username",
            state = DISABLED
            )
        self.apply_style(self.username_label)
        self.username_label.grid(row = 0, column = 2, sticky = W)

        self.username_text_box = Entry(self.window, state = DISABLED)
        self.username_text_box.grid(row = 0, column = 3)
        self.apply_style(self.username_text_box)
        self.bind_data(self.username_text_box,  "username")

        self.password_label = Label(
            self.window,
            text = "Password",
            state = DISABLED
            )
        self.apply_style(self.password_label)
        self.password_label.grid(row = 1, column = 2, sticky = W)

        self.password_text_box = Entry(
            self.window,
            state = DISABLED,
            show = "*"
            )
        self.password_text_box.grid(row = 1, column = 3)
        self.apply_style(self.password_text_box)
        self.bind_data(self.password_text_box, "password")

        self.message_label = Label(self.window, text = "Message")
        self.apply_style(self.message_label)
        self.message_label.grid(row = 3, column = 0, sticky = W)

        self.message_box = Text(self.window)
        self.message_box.grid(
            row = 3,
            column = 1,
            columnspan = 3,
            padx = 10,
            pady = 10
            )

        self.send_button = Button(
            self.window,
            text="Send",
            command = self.send
            )
        self.send_button.grid(row = 4, column = 0, columnspan = 2)

        self.close_button = Button(
            self.window,
            text="Close",
            command = self.window.quit
            )
        self.close_button.grid(row = 4, column = 2)

        self.binding_button = Button(
            self.window,
            text="Show 2 way binding",
            command = self.change_model_values
            )
        self.binding_button.grid(row = 4, column = 3)

    def send(self):
        """ Pass the message down to the view model to be sent """
        # get all the text from the message box
        message = self.message_box.get(1.0, END)
        ok = self.context.send(message)
        if (not ok):
            self.error_box(self.context.error())
        else:
            # clear the message box and reset some parameters
            self.message_box.delete(1.0, END)
            self.context.recipient = ""
            self.context.password = ""

    def center_window(self, window, window_width, window_height):
        """
        Center window in the screen with size window_width x window_height
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    def error_box(self, error):
        """ Make a pop-up box to show an error."""
        self.window.grab_set()
        new_window = Toplevel(self.window)
        new_window.title("Error")
        self.center_window(new_window, 300, 90)
        self.apply_style(new_window)
        label = Label(new_window, text = error)
        self.apply_style(label)
        label.pack(side = TOP)
        ok_button = Button(
            new_window,
            text = "Close",
            command = new_window.destroy
            )
        ok_button.pack(side = BOTTOM)

    def show_hide_authentication(self):
        """
        Show or hide the username and password fields depending on whether the
        view model tells us authentication is needed
        """
        if (self.context.authentification):
            self.username_label.config(state = NORMAL)
            self.username_text_box.config(state = NORMAL)
            self.password_label.config(state = NORMAL)
            self.password_text_box.config(state = NORMAL)
        else:
            self.username_label.config(state = DISABLED)
            self.username_text_box.config(state = DISABLED)
            self.password_label.config(state = DISABLED)
            self.password_text_box.config(state = DISABLED)

    def change_model_values(self):
        """
        Changes the values in the model so you can test if the bindings
        work properly. Note only view_model properties changed and the view
        updates.
        """
        self.context.server = "Has"
        self.context.recipient = "this"
        self.context.email = "changed?"
        self.context.authentification = not self.context.authentification
        self.context.username = "This should have"
        self.context.password = "changed, has it?"
        self.context.recipient_label = "Labels change too?!"

#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    # 13/06/12 Moved to main.py
    #--------------------------------------------------------------------------
    pass

