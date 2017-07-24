#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 24, 2017 08:35:16 AM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def buildUrlOut():
    print('exportPanel_support.buildUrlOut')
    sys.stdout.flush()

def pushDataSet():
    print('exportPanel_support.pushDataSet')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global wEx, top_levelEx, rootEx
    wEx = guiEx
    top_levelEx = topEx
    rootEx = topEx

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import exportPanel
    exportPanel.vp_start_gui()


