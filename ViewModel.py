#!/usr/bin/env python
# Written by: DGC

# the view model

import Model
from MVVM import NotifyPropertyChanged

#==============================================================================
class EmailViewModel(NotifyPropertyChanged):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    def __init__(self, model):
        self.model = model
        # check if Labels bind properly. They do!
        self._recipient_label = "To"

    @property
    def server(self):
        """Server property."""
        return self.model.server

    @server.setter
    def server(self, value):
        """Server property setter."""
        self.model.server = value
        self.on_property_changed("server")
     
    @property
    def email(self):
        """Email property."""
        return self.model.email

    @email.setter
    def email(self, value):
        """Server property setter."""
        self.model.email = value
        self.on_property_changed("email")
     
    @property
    def recipient(self):
        """Recipient property."""
        return self.model.recipient

    @recipient.setter
    def recipient(self, value):
        """Server property setter."""
        self.model.recipient = value
        self.on_property_changed("recipient")
     
    @property
    def username(self):
        """Username property."""
        return self.model.username

    @username.setter
    def username(self, value):
        """Server property setter."""
        self.model.username = value
        self.on_property_changed("username")
     
    @property
    def password(self):
        """Password property."""
        return self.model.password

    @password.setter
    def password(self, value):
        """Server property setter."""
        self.model.password = value
        self.on_property_changed("password")
     
    @property
    def authentification(self):
        """Authentification property."""
        return self.model.authenticate

    @authentification.setter
    def authentification(self, value):
        """Server property setter."""
        self.model.authenticate = value
        self.on_property_changed("authentification")
     
    @property
    def recipient_label(self):
        """Recipient property."""
        return self._recipient_label

    @recipient_label.setter
    def recipient_label(self, value):
        """Server property setter."""
        self._recipient_label = value
        self.on_property_changed("recipient_label")
     
    def error(self):
        """Error property."""
        return self.model.error()

    def send(self, message):
        """Returns an error if not sent for any reason"""
        message =  self.model.send(message)
        # everything changed
        self.on_property_changed("")
        return message

    def on_property_changed(self, property_name):
        self.property_changed(property_name)


#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    # a small test to check the view model still works. This is manual as it 
    # needs checking if the email arrives ok.
    model = Model.Email()
    sender = EmailViewModel(model)
    sender.server = "pat.delcam.com"
    sender.recipient = "davidcorne@gmail.com"
    sender.email = "dgc@delcam.com"
    if (not sender.send("View Model Class test 1")):
        print(sender.error())
