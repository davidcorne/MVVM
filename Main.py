#!/usr/bin/env python
# Written by: DGC

# runs the MVVM example
import Model
import ViewModel
import View

import sys
# renamed module in python 3
if (sys.version_info[:2] < (3,0)):
    from Tkinter import Tk
else:
    from tkinter import Tk


#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    root = Tk()
    model = Model.Email()
    sender = ViewModel.EmailViewModel(model)
    app = View.TKinterView(root, sender)
    root.withdraw()
    root.mainloop()
    
