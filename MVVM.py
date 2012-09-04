#!/usr/bin/env python
# Written by: DGC

# TKinter specific MVVM instrumentation helper functions

import abc

import sys
# renamed module in python 3
if (sys.version_info[:2] < (3,0)):
    from Tkinter import *
else:
    from tkinter import *
from Style import Style
from xml.dom.minidom import parseString

#==============================================================================
class NotifyPropertyChanged(object):
    #__metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def on_property_changed(self, property_name):
        return

    def property_changed(self, property_name):
        """Tell the view that property_name has changed"""
        # if property_changed("") is called all properties should be updated
        single = ViewCollection()
        if (property_name == ""):
            self.all_properties_changed()
            return
        for view in single.views:
            if (property_name in view.properties):
                view.property_changed(property_name)

    def all_properties_changed(self):
        """Tell the view that all the properties have changed"""
        single = ViewCollection()
        for view in single.views:
            for prop in view.properties:
                view.property_changed(prop)

#==============================================================================
class Singleton(object):
    """ A generic base class to derive any singleton class from. """
    __instance = None

    def __new__(new_singleton, *arguments, **keyword_arguments):
        """Override the __new__ method so that it is a singleton."""
        if not new_singleton.__instance:
            new_singleton.__instance = object.__new__(new_singleton)
            new_singleton.__instance.__init__(*arguments, **keyword_arguments)
        return new_singleton.__instance

#==============================================================================
class ViewCollection(Singleton):
    instance = None
    views = []

    def __init__(self):
        pass

    def add(self, view):
        self.views.append(view)

#==============================================================================
class View(object):

    def __init__(self):
        view = ViewCollection()
        view.add(self)
        self.properties = dict()

    def property_changed(self, property_name):
        """This will re-read the given property in the view"""
        if (isinstance(self.properties[property_name], Entry)):
            # insert the new value in the entry
            self.properties[property_name].delete(0, END)
            self.properties[property_name].insert(
                0,
                getattr(self.context, property_name)
                )

        elif (isinstance(self.properties[property_name], Checkbutton)):
            # check/uncheck the check button then run it's requisite function
            if (getattr(self.context, property_name)):
                self.properties[property_name].select()
            else:
                self.properties[property_name].deselect()
            self.properties[property_name].invoke()

        elif (isinstance(self.properties[property_name], Label)):
            # set the label text
            self.properties[property_name].config(
                text = str(getattr(self.context, property_name))
                )

    def bind_data(self, widget, property_name):
        """
        This function binds a function to a widget and sets the callback
        function. For things which are sensible this is 2 way binding.
        (anything editable i.e not a Label)
        """
        # unpythonic code, used for generic data binding as there are different
        # behaviours for different widgets

        # if the widget is an Entry
        if (isinstance(widget, Entry)):
            # bind any key press to setting the contents of the widget to the
            # property
            widget.bind(
                "<KeyRelease>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    event.widget.get()
                    )
                )
        # if the widget is a check button
        if (isinstance(widget, Checkbutton)):
            # a binary value has to be bound to this, calls not on the value
            widget.bind(
                "<Button-1>",
                lambda event: setattr(
                    self.context,
                    property_name,
                    (not getattr(self.context, property_name))
                    )
                )
        # a one way binding to the text in a label
        if (isinstance(widget, Label)):
            # sets the label text to be the property
            widget.config(text = str(getattr(self.context, property_name)))

        # add the widget to the properties list
        self.properties[property_name] = widget

    def apply_style(self, widget):
        """Sets the specific styles for each widget type"""
        s = Style(self.style)
        s.apply_style(widget)

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
