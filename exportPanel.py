#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 24, 2017 08:35:20 AM
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

import exportPanel_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global valEx, wEx, rootEx
    rootEx = Tk()
    top = Export(rootEx)
    exportPanel_support.init(rootEx, top)
    rootEx.mainloop()

w = None
def create_Export(rootEx, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global wEx, w_win, rt
    rt = rootEx
    wEx = Toplevel (rootEx)
    top = Export (wEx)
    exportPanel_support.init(wEx, top, *args, **kwargs)
    return (wEx, top)

def destroy_Export():
    global wEx
    wEx.destroy()
    wEx = None


class Export:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#00407f' # Closest X11 color: 'DodgerBlue4'
        _ana1color = '#7f7f00' # Closest X11 color: 'gold4' 
        _ana2color = '#7f0000' # Closest X11 color: 'red4' 
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.style.map('.',foreground=
            [('selected', 'white'), ('active','white')])

        top.geometry("600x333")
        top.title("Export")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.02, rely=0.03, relheight=0.56
                , relwidth=0.33)
        self.TLabelframe1.configure(text='''Output User Info''')
        self.TLabelframe1.configure(width=200)

        self.usernameOutEnt = ttk.Entry(self.TLabelframe1)
        self.usernameOutEnt.place(relx=0.05, rely=0.32, relheight=0.14
                , relwidth=0.83)
        self.usernameOutEnt.configure(takefocus="")
        self.usernameOutEnt.configure(cursor="ibeam")

        self.passwordOutEnt = ttk.Entry(self.TLabelframe1)
        self.passwordOutEnt.place(relx=0.05, rely=0.76, relheight=0.14
                , relwidth=0.83)
        self.passwordOutEnt.configure(takefocus="")
        self.passwordOutEnt.configure(cursor="ibeam")

        self.usernameOutLab = ttk.Label(self.TLabelframe1)
        self.usernameOutLab.place(relx=0.05, rely=0.16, height=24, width=70)
        self.usernameOutLab.configure(background="#d9d9d9")
        self.usernameOutLab.configure(foreground="#000000")
        self.usernameOutLab.configure(relief=FLAT)
        self.usernameOutLab.configure(text='''Username''')

        self.passwordOutLab = ttk.Label(self.TLabelframe1)
        self.passwordOutLab.place(relx=0.05, rely=0.54, height=24, width=66)
        self.passwordOutLab.configure(background="#d9d9d9")
        self.passwordOutLab.configure(foreground="#000000")
        self.passwordOutLab.configure(relief=FLAT)
        self.passwordOutLab.configure(text='''Password''')

        self.urlOutLabFrame = ttk.Labelframe(top)
        self.urlOutLabFrame.place(relx=0.37, rely=0.03, relheight=0.56
                , relwidth=0.58)
        self.urlOutLabFrame.configure(text='''Url Selection''')
        self.urlOutLabFrame.configure(width=350)

        self.projectOutEnt = ttk.Entry(self.urlOutLabFrame)
        self.projectOutEnt.place(relx=0.03, rely=0.32, relheight=0.14
                , relwidth=0.47)
        self.projectOutEnt.configure(takefocus="")
        self.projectOutEnt.configure(cursor="ibeam")

        self.projectOutLab = ttk.Label(self.urlOutLabFrame)
        self.projectOutLab.place(relx=0.03, rely=0.16, height=24, width=50)
        self.projectOutLab.configure(background="#d9d9d9")
        self.projectOutLab.configure(foreground="#000000")
        self.projectOutLab.configure(relief=FLAT)
        self.projectOutLab.configure(text='''Project''')

        self.urlOutEnt = ttk.Entry(self.urlOutLabFrame)
        self.urlOutEnt.place(relx=0.03, rely=0.76, relheight=0.14, relwidth=0.7)
        self.urlOutEnt.configure(takefocus="")
        self.urlOutEnt.configure(cursor="ibeam")

        self.buildUrlOutButton = ttk.Button(self.urlOutLabFrame)
        self.buildUrlOutButton.place(relx=0.57, rely=0.32, height=30, width=98)
        self.buildUrlOutButton.configure(command=exportPanel_support.buildUrlOut)
        self.buildUrlOutButton.configure(takefocus="")
        self.buildUrlOutButton.configure(text='''Build Url''')

        self.urlOutLab = ttk.Label(self.urlOutLabFrame)
        self.urlOutLab.place(relx=0.03, rely=0.54, height=24, width=30)
        self.urlOutLab.configure(background="#d9d9d9")
        self.urlOutLab.configure(foreground="#000000")
        self.urlOutLab.configure(relief=FLAT)
        self.urlOutLab.configure(text='''URL''')

        self.pushDataButton = ttk.Button(self.urlOutLabFrame)
        self.pushDataButton.place(relx=0.77, rely=0.76, height=30, width=58)
        self.pushDataButton.configure(command=exportPanel_support.pushDataSet)
        self.pushDataButton.configure(takefocus="")
        self.pushDataButton.configure(text='''Export''')

        self.optionalOutLabFrame = ttk.Labelframe(top)
        self.optionalOutLabFrame.place(relx=0.02, rely=0.6, relheight=0.32
                , relwidth=0.33)
        self.optionalOutLabFrame.configure(text='''Optional''')
        self.optionalOutLabFrame.configure(width=200)

        self.renameSeriesEnt = ttk.Entry(self.optionalOutLabFrame)
        self.renameSeriesEnt.place(relx=0.05, rely=0.57, relheight=0.25
                , relwidth=0.83)
        self.renameSeriesEnt.configure(takefocus="")
        self.renameSeriesEnt.configure(cursor="ibeam")

        self.renameLab = ttk.Label(self.optionalOutLabFrame)
        self.renameLab.place(relx=0.05, rely=0.29, height=24, width=121)
        self.renameLab.configure(background="#d9d9d9")
        self.renameLab.configure(foreground="#000000")
        self.renameLab.configure(relief=FLAT)
        self.renameLab.configure(text='''New Series Name''')

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()



