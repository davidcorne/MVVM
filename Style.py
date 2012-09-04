#!/usr/bin/env python
# Written by: DGC

from xml.dom.minidom import parseString
import sys
import os
# renamed module in python 3
if (sys.version_info[:2] < (3,0)):
    from Tkinter import *
else:
    from tkinter import *

#==============================================================================
class Style(object):

    def __init__(self, style):
        self.style = style
        self.__read_style()

    def __read_style(self):
        """
        Reads style information in from an xml document in the same directory
        called style.xml
        """
        # open the file, convert it to a string then close it
        directory = os.path.dirname(str(sys.argv[0]))
        if (directory):
            file_location = directory + "/Style.xml"
        else:
            file_location = "Style.xml"
        style_file = open(file_location, "r")
        data = style_file.read()
        style_file.close()

        # parse the xml
        dom = parseString(data)
        self.style_codes = []
        style_node = self.__get_style_node(self.style, dom)
        assert style_node, "Style node not found."
        for widget in style_node.childNodes:
            for tag in widget.childNodes:
                # if it is an attribute node
                if (tag.nodeType == 1):
                    self.style_codes.append(
                        [widget.nodeName, tag.nodeName,tag.firstChild.data]
                        )


    def __get_style_node(self, style, data):
        """Returns the <Style> node with Name == style"""
        styles = data.getElementsByTagName("Style")
        for node in styles:
            for i in range(0, node.attributes.length):
                if (node.attributes.item(i).name == "Name"):
                    if (node.attributes.item(i).value == style):
                        return node
        return []

    def apply_style(self, widget):
        """Sets the specific styles for each widget type"""
        if (isinstance(widget, Button)):
            self.__apply_style("Button", widget)

        elif (isinstance(widget, Canvas)):
            self.__apply_style("Canvas", widget)

        elif (isinstance(widget, Checkbutton)):
            self.__apply_style("Checkbutton", widget)

        elif (isinstance(widget, Entry)):
            self.__apply_style("Entry", widget)

        elif (isinstance(widget, Frame)):
            self.__apply_style("Frame", widget)

        elif (isinstance(widget, Label)):
            self.__apply_style("Label", widget)

        elif (isinstance(widget, LabelFrame)):
            self.__apply_style("LabelFrame", widget)

        elif (isinstance(widget, Listbox)):
            self.__apply_style("Listbox", widget)

        elif (isinstance(widget, Menu)):
            self.__apply_style("Menu", widget)

        elif (isinstance(widget, Menubutton)):
            self.__apply_style("Menubutton", widget)

        elif (isinstance(widget, Message)):
            self.__apply_style("Message", widget)

        elif (isinstance(widget, OptionMenu)):
            self.__apply_style("OptionMenu", widget)

        elif (isinstance(widget, PanedWindow)):
            self.__apply_style("PanedWindow", widget)

        elif (isinstance(widget, Radiobutton)):
            self.__apply_style("Radiobutton", widget)

        elif (isinstance(widget, Scale)):
            self.__apply_style("Scale", widget)

        elif (isinstance(widget, Scrollbar)):
            self.__apply_style("Scrollbar", widget)

        elif (isinstance(widget, Spinbox)):
            self.__apply_style("Spinbox", widget)

        elif (isinstance(widget, Text)):
            self.__apply_style("Text", widget)

        elif (isinstance(widget, Tk)):
            self.__apply_style("Tk", widget)

        elif (isinstance(widget, Toplevel)):
            self.__apply_style("Toplevel", widget)

        else:
            print("not found")

    def __apply_style(self, widget_type, widget):
        """Applies the style from self.style """
        for code in self.style_codes:
            if (code[0] == widget_type):
                if (code[1] == "Accelerator"):
                    widget.configure(accelerator = code[2])

                elif (code[1] == "Activebackground"):
                    widget.configure(activebackground = code[2])

                elif (code[1] == "Activeforeground"):
                    widget.configure(activeforeground = code[2])

                elif (code[1] == "Activerelief"):
                    widget.configure(activerelief = code[2])

                elif (code[1] == "Activestyle"):
                    widget.configure(activestyle = code[2])

                elif (code[1] == "Anchor"):
                    widget.configure(anchor = code[2])

                elif (code[1] == "Aspect"):
                    widget.configure(aspect = code[2])

                elif (code[1] == "Autoseparators"):
                    widget.configure(autoseparators = code[2])

                elif (code[1] == "Background"):
                    widget.configure(background = code[2])

                elif (code[1] == "Bigincrement"):
                    widget.configure(bigincrement = code[2])

                elif (code[1] == "Bitmap"):
                    widget.configure(bitmap = code[2])

                elif (code[1] == "Borderwidth"):
                    widget.configure(borderwidth = code[2])

                elif (code[1] == "Buttonbackground"):
                    widget.configure(buttonbackground = code[2])

                elif (code[1] == "Buttoncursor"):
                    widget.configure(buttoncursor = code[2])

                elif (code[1] == "Buttondownrelief"):
                    widget.configure(buttondownrelief = code[2])

                elif (code[1] == "Buttonuprelief"):
                    widget.configure(buttonuprelief = code[2])

                    #elif (code[1] == "class"):
                    #    widget.configure(class = code[2])

                elif (code[1] == "Closeenough"):
                    widget.configure(closeenough = code[2])

                elif (code[1] == "Colormap"):
                    widget.configure(colormap = code[2])

                elif (code[1] == "Columnbreak"):
                    widget.configure(columnbreak = code[2])

                elif (code[1] == "Command"):
                    widget.configure(command = code[2])

                elif (code[1] == "Compound"):
                    widget.configure(compound = code[2])

                elif (code[1] == "Confine"):
                    widget.configure(confine = code[2])

                elif (code[1] == "Container"):
                    widget.configure(container = code[2])

                elif (code[1] == "Cursor"):
                    widget.configure(cursor = code[2])

                elif (code[1] == "Default"):
                    widget.configure(default = code[2])

                elif (code[1] == "Digits"):
                    widget.configure(digits = code[2])

                elif (code[1] == "Direction"):
                    widget.configure(direction = code[2])

                elif (code[1] == "Disabledbackground"):
                    widget.configure(disabledbackground = code[2])

                elif (code[1] == "Disabledforeground"):
                    widget.configure(disabledforeground = code[2])

                elif (code[1] == "Elementborderwidth"):
                    widget.configure(elementborderwidth = code[2])

                elif (code[1] == "Exportselection"):
                    widget.configure(exportselection = code[2])

                elif (code[1] == "Font"):
                    widget.configure(font = code[2])

                elif (code[1] == "Foreground"):
                    widget.configure(foreground = code[2])

                elif (code[1] == "Format"):
                    widget.configure(format = code[2])

                    #elif (code[1] == "from"):
                    #    widget.configure(from = code[2])

                elif (code[1] == "Handlepad"):
                    widget.configure(handlepad = code[2])

                elif (code[1] == "Handlesize"):
                    widget.configure(handlesize = code[2])

                elif (code[1] == "Height"):
                    widget.configure(height = code[2])

                elif (code[1] == "Hidemargin"):
                    widget.configure(hidemargin = code[2])

                elif (code[1] == "Highlightbackground"):
                    widget.configure(highlightbackground = code[2])

                elif (code[1] == "Highlightcolor"):
                    widget.configure(highlightcolor = code[2])

                elif (code[1] == "Highlightthickness"):
                    widget.configure(highlightthickness = code[2])

                elif (code[1] == "Image"):
                    widget.configure(image = code[2])

                elif (code[1] == "Increment"):
                    widget.configure(increment = code[2])

                elif (code[1] == "Indicatoron"):
                    widget.configure(indicatoron = code[2])

                elif (code[1] == "Insertbackground"):
                    widget.configure(insertbackground = code[2])

                elif (code[1] == "Insertborderwidth"):
                    widget.configure(insertborderwidth = code[2])

                elif (code[1] == "Insertofftime"):
                    widget.configure(insertofftime = code[2])

                elif (code[1] == "Insertontime"):
                    widget.configure(insertontime = code[2])

                elif (code[1] == "Insertwidth"):
                    widget.configure(insertwidth = code[2])

                elif (code[1] == "Invalidcommand"):
                    widget.configure(invalidcommand = code[2])

                elif (code[1] == "Invcmd"):
                    widget.configure(invcmd = code[2])

                elif (code[1] == "Jump"):
                    widget.configure(jump = code[2])

                elif (code[1] == "Justify"):
                    widget.configure(justify = code[2])

                elif (code[1] == "Label"):
                    widget.configure(label = code[2])

                elif (code[1] == "Labelanchor"):
                    widget.configure(labelanchor = code[2])

                elif (code[1] == "Labelwidget"):
                    widget.configure(labelwidget = code[2])

                elif (code[1] == "Length"):
                    widget.configure(length = code[2])

                elif (code[1] == "Listvariable"):
                    widget.configure(listvariable = code[2])

                elif (code[1] == "Maxundo"):
                    widget.configure(maxundo = code[2])

                elif (code[1] == "Menu"):
                    widget.configure(menu = code[2])

                elif (code[1] == "Offrelief"):
                    widget.configure(offrelief = code[2])

                elif (code[1] == "Offset"):
                    widget.configure(offset = code[2])

                elif (code[1] == "Offvalue"):
                    widget.configure(offvalue = code[2])

                elif (code[1] == "Onvalue"):
                    widget.configure(onvalue = code[2])

                elif (code[1] == "Opaqueresize"):
                    widget.configure(opaqueresize = code[2])

                elif (code[1] == "Orient"):
                    widget.configure(orient = code[2])

                elif (code[1] == "Overrelief"):
                    widget.configure(overrelief = code[2])

                elif (code[1] == "Padx"):
                    widget.configure(padx = code[2])

                elif (code[1] == "Pady"):
                    widget.configure(pady = code[2])

                elif (code[1] == "Readonlybackground"):
                    widget.configure(readonlybackground = code[2])

                elif (code[1] == "Relief"):
                    widget.configure(relief = code[2])

                elif (code[1] == "Repeatdelay"):
                    widget.configure(repeatdelay = code[2])

                elif (code[1] == "Repeatinterval"):
                    widget.configure(repeatinterval = code[2])

                elif (code[1] == "Resolution"):
                    widget.configure(resolution = code[2])

                elif (code[1] == "Sashcursor"):
                    widget.configure(sashcursor = code[2])

                elif (code[1] == "Sashpad"):
                    widget.configure(sashpad = code[2])

                elif (code[1] == "Sashrelief"):
                    widget.configure(sashrelief = code[2])

                elif (code[1] == "Sashwidth"):
                    widget.configure(sashwidth = code[2])

                elif (code[1] == "Screen"):
                    widget.configure(screen = code[2])

                elif (code[1] == "Scrollregion"):
                    widget.configure(scrollregion = code[2])

                elif (code[1] == "Selectbackground"):
                    widget.configure(selectbackground = code[2])

                elif (code[1] == "Selectborderwidth"):
                    widget.configure(selectborderwidth = code[2])

                elif (code[1] == "Selectcolor"):
                    widget.configure(selectcolor = code[2])

                elif (code[1] == "Selectforeground"):
                    widget.configure(selectforeground = code[2])

                elif (code[1] == "Selectimage"):
                    widget.configure(selectimage = code[2])

                elif (code[1] == "Selectmode"):
                    widget.configure(selectmode = code[2])

                elif (code[1] == "Setgrid"):
                    widget.configure(setgrid = code[2])

                elif (code[1] == "Show"):
                    widget.configure(show = code[2])

                elif (code[1] == "Showhandle"):
                    widget.configure(showhandle = code[2])

                elif (code[1] == "Showvalue"):
                    widget.configure(showvalue = code[2])

                elif (code[1] == "Sliderlength"):
                    widget.configure(sliderlength = code[2])

                elif (code[1] == "Sliderrelief"):
                    widget.configure(sliderrelief = code[2])

                elif (code[1] == "Spacing1"):
                    widget.configure(spacing1 = code[2])

                elif (code[1] == "Spacing2"):
                    widget.configure(spacing2 = code[2])

                elif (code[1] == "Spacing3"):
                    widget.configure(spacing3 = code[2])

                elif (code[1] == "State"):
                    widget.configure(state = code[2])

                elif (code[1] == "Tabs"):
                    widget.configure(tabs = code[2])

                elif (code[1] == "Takefocus"):
                    widget.configure(takefocus = code[2])

                elif (code[1] == "Text"):
                    widget.configure(text = code[2])

                elif (code[1] == "Textvariable"):
                    widget.configure(textvariable = code[2])

                elif (code[1] == "Tickinterval"):
                    widget.configure(tickinterval = code[2])

                elif (code[1] == "To"):
                    widget.configure(to = code[2])

                elif (code[1] == "Troughcolor"):
                    widget.configure(troughcolor = code[2])

                elif (code[1] == "Underline"):
                    widget.configure(underline = code[2])

                elif (code[1] == "Undo"):
                    widget.configure(undo = code[2])

                elif (code[1] == "Use"):
                    widget.configure(use = code[2])

                elif (code[1] == "Validate"):
                    widget.configure(validate = code[2])

                elif (code[1] == "Validatecommand"):
                    widget.configure(validatecommand = code[2])

                elif (code[1] == "Value"):
                    widget.configure(value = code[2])

                elif (code[1] == "Values"):
                    widget.configure(values = code[2])

                elif (code[1] == "Variable"):
                    widget.configure(variable = code[2])

                elif (code[1] == "Vcmd"):
                    widget.configure(vcmd = code[2])

                elif (code[1] == "Visual"):
                    widget.configure(visual = code[2])

                elif (code[1] == "Vidth"):
                    widget.configure(width = code[2])

                elif (code[1] == "Vrap"):
                    widget.configure(wrap = code[2])

                elif (code[1] == "Wraplength"):
                    widget.configure(wraplength = code[2])

                elif (code[1] == "Xscrollcommand"):
                    widget.configure(xscrollcommand = code[2])

                elif (code[1] == "Xscrollincrement"):
                    widget.configure(xscrollincrement = code[2])

                elif (code[1] == "Yscrollcommand"):
                    widget.configure(yscrollcommand = code[2])

                elif (code[1] == "Yscrollincrement"):
                    widget.configure(yscrollincrement = code[2])

                else:
                    print("Unknown attribute set")
                    assert(False)

#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 15/06/12 Written.
    #--------------------------------------------------------------------------
    print(read_style("DGC"))
