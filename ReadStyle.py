#!/usr/bin/env python
# Written by: DGC

from xml.dom.minidom import parseString

#==============================================================================
def read_style(style):
    """
    Reads style information in from an xml document in the same directory
    called style.xml
    """
    # open the file, convert it to a string then close it
    style_file = open("style.xml","r")
    data = style_file.read()
    style_file.close()

    #parse the xml
    dom = parseString(data)
    style_codes = []
    style_node = get_style_node(style, dom)
    if (not style_node):
        return style_codes
    for widget in style_node.childNodes:
        for tag in widget.childNodes:
            # if it is an attribute node
            if (tag.nodeType == 1):
                style_codes.append(
                    [widget.nodeName, tag.nodeName,tag.firstChild.data]
                    )
    return style_codes
                

#==============================================================================
def get_style_node(style, data):
    """Returns the <Style> node with Name == style"""
    styles = data.getElementsByTagName("Style")
    for node in styles:
        for i in range(0, node.attributes.length):
            if (node.attributes.item(i).name == "Name"):
                if (node.attributes.item(i).value == style):
                    return node
    return []

#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 15/06/12 Written.
    #--------------------------------------------------------------------------
    print(read_style("DGC"))
