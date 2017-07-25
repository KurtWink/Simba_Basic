#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 24, 2017 07:59:26 AM
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

import Simba_support
rootEx = None
rootHs = None
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    Simba_support.set_Tk_var()
    top = Simba (root)
    Simba_support.init(root, top)

    def closeAll():
        if rootEx is not None:
            try:
                rootEx.destroy()
            except:
                pass
        if rootHs is not None:
            try:
                rootHs.destroy()
            except:
                pass

        root.destroy()

    root.protocol("WM_DELETE_WINDOW", closeAll)
    root.mainloop()

w = None
wEx = None
wHs = None
def create_Simba(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    Simba_support.set_Tk_var()
    top = Simba (w)
    Simba_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Simba():
    global w
    w.destroy()
    w = None
    global wEx
    wEx.destroy()
    wEx = None
    global wHs
    wHs.destroy()
    wHs = None

#Class for main Simba Frame
class Simba:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#00407f' # Closest X11 color: 'DodgerBlue4'
        _ana1color = '#7f7f00' # Closest X11 color: 'gold4' 
        _ana2color = '#7f0000' # Closest X11 color: 'red4' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
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

        top.geometry("699x509")
        top.title("Simba")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False,False)






        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                activebackground="#7f0000",
                activeforeground="#111111",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="File")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=Simba_support.clearData,
                font=font9,
                foreground="#000000",
                label="Clear Data",
                state=DISABLED)
        self.file.add_separator(
                background="#d9d9d9")

        self.open_from = Menu(top,tearoff=0)
        self.file.add_cascade(menu=self.open_from,
                activebackground="#7f0000",
                activeforeground="#111111",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Open From")
        self.open_from.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=Simba_support.getLocalData,
                font=font9,
                foreground="#000000",
                label="Local File")
        self.open_from.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda: openHostPanel(),
                font=font9,
                foreground="#000000",
                label="Hosted Service")
        self.file.add_separator(
                background="#d9d9d9")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=Simba_support.saveLocalData,
                font=font9,
                foreground="#000000",
                label="Save As",
                state=DISABLED)
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:openExportPanel(),
                font=font9,
                foreground="#000000",
                label="Export",
                state=DISABLED)
        self.modules = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.modules,
                activebackground="#7f0000",
                activeforeground="#111111",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Modules")
        self.modules.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=lambda:populateCombo(),
                font=font9,
                foreground="#000000",
                label="Import Module")
        self.help = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.help,
                activebackground="#7f0000",
                activeforeground="#111111",
                background="#d9d9d9",
                font=font9,
                foreground="#000000",
                label="Help")
        self.help.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=Simba_support.openHelp,
                font=font9,
                foreground="#000000",
                label="Main Docs")


        self.mainSimbaFrame = ttk.Frame(top)
        self.mainSimbaFrame.place(relx=0.0, rely=0.0, relheight=1.01, relwidth=1.01)
        self.mainSimbaFrame.configure(relief=GROOVE)
        self.mainSimbaFrame.configure(borderwidth="2")
        self.mainSimbaFrame.configure(relief=GROOVE)
        self.mainSimbaFrame.configure(width=705)
        self.mainSimbaFrame.configure(takefocus="0")

        self.varListBox = tagListBox(self.mainSimbaFrame)
        self.varListBox.place(relx=0.01, rely=0.08, relheight=0.81
                , relwidth=0.46)
        self.varListBox.configure(background="white")
        self.varListBox.configure(disabledforeground="#a3a3a3")
        self.varListBox.configure(font=font10)
        self.varListBox.configure(foreground="black")
        self.varListBox.configure(highlightbackground="#d9d9d9")
        self.varListBox.configure(highlightcolor="#d9d9d9")
        self.varListBox.configure(selectbackground="#c4c4c4")
        self.varListBox.configure(selectforeground="black")
        self.varListBox.configure(takefocus="0")
        self.varListBox.configure(width=10)

        self.tagListBox2 = tagListBox(self.mainSimbaFrame)
        self.tagListBox2.place(relx=0.5, rely=0.08, relheight=0.81
                , relwidth=0.46)
        self.tagListBox2.configure(background="white")
        self.tagListBox2.configure(disabledforeground="#a3a3a3")
        self.tagListBox2.configure(font=font10)
        self.tagListBox2.configure(foreground="black")
        self.tagListBox2.configure(highlightbackground="#d9d9d9")
        self.tagListBox2.configure(highlightcolor="#d9d9d9")
        self.tagListBox2.configure(selectbackground="#c4c4c4")
        self.tagListBox2.configure(selectforeground="black")
        self.tagListBox2.configure(takefocus="0")
        self.tagListBox2.configure(width=10)

        self.dataOpCombo = ttk.Combobox(self.mainSimbaFrame)
        self.dataOpCombo.place(relx=0.5, rely=0.89, relheight=0.05
                , relwidth=0.29)
        self.dataOpCombo.configure(textvariable=Simba_support.combobox)
        self.dataOpCombo.configure(takefocus="",state="readonly")

        def populateCombo():
            Simba_support.loadMod()
            listCol=[x.name for x in (Simba_support.getMod())()]
            self.dataOpCombo.configure(values=listCol)

        def onselect(evt):
            # Note here that Tkinter passes an event object to onselect()
            self.varListBox.delete(0, END)

            w = evt.widget
            index = int(w.current())
            # Populating Varboxes on select

            for n in (Simba_support.getMod())()[index].vars:

                self.varListBox.insert(END, str(n.name) + str(n.value))
                # value = w.get(index)
        self.dataOpCombo.bind('<<ComboboxSelected>>', onselect)
        self.varListBox.configure(exportselection=False)
        def editVar():
                #Simba_support.setModVars(0,0)

                #List of MethodObjects
                func = Simba_support.getMod()()
                print(func)
                #List of var objects
                func2 = func[0].vars
                print(func2)

                (func[self.dataOpCombo.current()].vars[
                    self.varListBox.curselection()[0]].value) = Simba_support.editVarVar.get()
                print(Simba_support.getEditVar())
                print(func[self.dataOpCombo.current()].vars[
                          self.varListBox.curselection()[0]].value)
                Simba_support.checkVal()


                """
                (Simba_support.getMod())()[self.dataOpCombo.current()].vars[
                    self.varListBox.curselection()[0]].value = Simba_support.editVarVar
                print(Simba_support.getEditVar())
                print((Simba_support.getMod())()[self.dataOpCombo.current()].vars[
                    self.varListBox.curselection()[0]].value)
                """
                self.varListBox.delete(0, END)


                for n in func[self.dataOpCombo.current()].vars:
                    print(n.name)
                    self.varListBox.insert(END, str(n.name) + str(n.value))





        self.setVarButton = ttk.Button(self.mainSimbaFrame)
        self.setVarButton.place(relx=0.37, rely=0.89, height=30, width=78)
        self.setVarButton.configure(takefocus="")
        self.setVarButton.configure(text='''Set''')
        self.setVarButton.configure(command=lambda:editVar())

        self.setVarEnt = ttk.Entry(self.mainSimbaFrame)
        self.setVarEnt.place(relx=0.03, rely=0.89, relheight=0.05, relwidth=0.32)
        self.setVarEnt.configure(textvariable=Simba_support.editVarVar)
        self.setVarEnt.configure(takefocus="")
        self.setVarEnt.configure(cursor="ibeam")

        self.dataOpButton = ttk.Button(self.mainSimbaFrame)
        self.dataOpButton.place(relx=0.82, rely=0.89, height=30, width=78)
        self.dataOpButton.configure(takefocus="")
        self.dataOpButton.configure(text='''Apply''')

        self.varListLab = ttk.Label(self.mainSimbaFrame)
        self.varListLab.place(relx=0.17, rely=0.02, height=24, width=85)
        self.varListLab.configure(background="#d9d9d9")
        self.varListLab.configure(foreground="#000000")
        self.varListLab.configure(relief=FLAT)
        self.varListLab.configure(takefocus="0")
        self.varListLab.configure(text='''Variable List''')

        self.tagsListLab = ttk.Label(self.mainSimbaFrame)
        self.tagsListLab.place(relx=0.67, rely=0.02, height=24, width=71)
        self.tagsListLab.configure(background="#d9d9d9")
        self.tagsListLab.configure(foreground="#000000")
        self.tagsListLab.configure(relief=FLAT)
        self.tagsListLab.configure(takefocus="0")
        self.tagsListLab.configure(text='''Data Tags''')

        self.loadBar = ttk.Progressbar(self.mainSimbaFrame)
        self.loadBar.place(relx=0.01, rely=0.02, relwidth=0.07, relheight=0.0
                , height=22)
        self.loadBar.configure(variable=Simba_support.loadBarVar)
        self.loadBar.configure(takefocus="0")

        # Sub Panel Methods

        #Sub Panel Checks to avoid making Singleton Pattern
        self.countExport =False
        self.countHost = False
        # Sub Window for the exporting to hosted service
        def closeSub(flip):
            flip = False

        def openExportPanel():

            def initEx(topEx, guiEx, *args, **kwargs):
                global wEx, top_levelEx, rootEx
                wEx = guiEx
                top_levelEx = topEx
                rootEx = topEx

            global valEx, wEx, rootEx
            rootEx = Tk()
            topEx = Export(rootEx)
            initEx(rootEx, topEx)
            rootEx.mainloop()



        # Sub window for log/pulling data from hosted service
        def openHostPanel():

            def initHs(topHs, guiHs, *args, **kwargs):
                global wHs, top_levelHs, rootHs
                wHs = guiHs
                top_levelHs = topHs
                rootHs = topHs

            global valHs, wHs, rootHs
            rootHs = Tk()
            topHs = Hosted_Service(rootHs)
            initHs(rootHs, topHs)
            rootHs.mainloop()







#Class for export Frame
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
        self.usernameOutEnt.configure(textvariable=Simba_support.usernameOutVar)
        self.usernameOutEnt.configure(takefocus="")
        self.usernameOutEnt.configure(cursor="ibeam")

        self.passwordOutEnt = ttk.Entry(self.TLabelframe1)
        self.passwordOutEnt.place(relx=0.05, rely=0.76, relheight=0.14
                , relwidth=0.83)
        self.passwordOutEnt.configure(textvariable=Simba_support.passwordOutVar)
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
        self.projectOutEnt.configure(textvariable=Simba_support.projectOutVar)
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
        self.urlOutEnt.configure(textvariable=Simba_support.urlOutVar)
        self.urlOutEnt.configure(takefocus="")
        self.urlOutEnt.configure(cursor="ibeam")

        self.buildUrlOutButton = ttk.Button(self.urlOutLabFrame)
        self.buildUrlOutButton.place(relx=0.57, rely=0.32, height=30, width=98)
        self.buildUrlOutButton.configure(command=Simba_support.buildUrlOut)
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
        self.pushDataButton.configure(command=Simba_support.pushDataSet)
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
        self.renameSeriesEnt.configure(textvariable=Simba_support.nameChangeVar)
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


#Class for HostedService Frame
class Hosted_Service:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#00407f' # Closest X11 color: 'DodgerBlue4'
        _ana1color = '#7f7f00' # Closest X11 color: 'gold4'
        _ana2color = '#7f0000' # Closest X11 color: 'red4'
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

        top.geometry("641x480")
        top.title("Hosted Service")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.selectLabFrame = ttk.Labelframe(top)
        self.selectLabFrame.place(relx=0.02, rely=0.0, relheight=0.47
                , relwidth=0.33)
        self.selectLabFrame.configure(text='''Input Project Selector''')
        self.selectLabFrame.configure(width=210)

        self.projectOutputEnt = ttk.Entry(self.selectLabFrame)
        self.projectOutputEnt.place(relx=0.05, rely=0.27, relheight=0.12
                , relwidth=0.79)
        self.projectOutputEnt.configure(textvariable=Simba_support.projectInputVar)
        self.projectOutputEnt.configure(takefocus="")
        self.projectOutputEnt.configure(cursor="ibeam")

        self.seriesInputEnt = ttk.Entry(self.selectLabFrame)
        self.seriesInputEnt.place(relx=0.05, rely=0.62, relheight=0.12
                , relwidth=0.79)
        self.seriesInputEnt.configure(textvariable=Simba_support.seriesInputVar)
        self.seriesInputEnt.configure(takefocus="")
        self.seriesInputEnt.configure(cursor="ibeam")

        self.seriesInputLab = ttk.Label(self.selectLabFrame)
        self.seriesInputLab.place(relx=0.05, rely=0.44, height=24, width=43)
        self.seriesInputLab.configure(background="#d9d9d9")
        self.seriesInputLab.configure(foreground="#000000")
        self.seriesInputLab.configure(relief=FLAT)
        self.seriesInputLab.configure(text='''Series''')

        self.projectInputLab = ttk.Label(self.selectLabFrame)
        self.projectInputLab.place(relx=0.05, rely=0.13, height=24, width=50)
        self.projectInputLab.configure(background="#d9d9d9")
        self.projectInputLab.configure(foreground="#000000")
        self.projectInputLab.configure(relief=FLAT)
        self.projectInputLab.configure(text='''Project''')

        self.buildURLButton = ttk.Button(self.selectLabFrame)
        self.buildURLButton.place(relx=0.05, rely=0.8, height=30, width=88)
        self.buildURLButton.configure(command=Simba_support.buildURL)
        self.buildURLButton.configure(takefocus="")
        self.buildURLButton.configure(text='''Create URL''')

        self.timeLabFrame = ttk.Labelframe(top)
        self.timeLabFrame.place(relx=0.36, rely=0.0, relheight=0.47
                , relwidth=0.59)
        self.timeLabFrame.configure(text='''Time Query''')
        self.timeLabFrame.configure(width=380)

        self.startingTimeStdEnt = ttk.Entry(self.timeLabFrame)
        self.startingTimeStdEnt.place(relx=0.03, rely=0.36, relheight=0.12
                , relwidth=0.41)
        self.startingTimeStdEnt.configure(textvariable=Simba_support.stdStartVar)
        self.startingTimeStdEnt.configure(takefocus="")
        self.startingTimeStdEnt.configure(cursor="ibeam")

        self.startingTimeEpoEnt = ttk.Entry(self.timeLabFrame)
        self.startingTimeEpoEnt.place(relx=0.5, rely=0.36, relheight=0.12
                , relwidth=0.41)
        self.startingTimeEpoEnt.configure(textvariable=Simba_support.epoStartVar)
        self.startingTimeEpoEnt.configure(takefocus="")
        self.startingTimeEpoEnt.configure(cursor="ibeam")

        self.endingTimeStdEnt = ttk.Entry(self.timeLabFrame)
        self.endingTimeStdEnt.place(relx=0.03, rely=0.67, relheight=0.12
                , relwidth=0.41)
        self.endingTimeStdEnt.configure(textvariable=Simba_support.stdEndVar)
        self.endingTimeStdEnt.configure(takefocus="")
        self.endingTimeStdEnt.configure(cursor="ibeam")

        self.endingTimeEpoEnt = ttk.Entry(self.timeLabFrame)
        self.endingTimeEpoEnt.place(relx=0.5, rely=0.67, relheight=0.12
                , relwidth=0.41)
        self.endingTimeEpoEnt.configure(textvariable=Simba_support.epoEndVar)
        self.endingTimeEpoEnt.configure(takefocus="")
        self.endingTimeEpoEnt.configure(cursor="ibeam")

        self.endTimeLab = ttk.Label(self.timeLabFrame)
        self.endTimeLab.place(relx=0.03, rely=0.53, height=24, width=87)
        self.endTimeLab.configure(background="#d9d9d9")
        self.endTimeLab.configure(foreground="#000000")
        self.endTimeLab.configure(relief=FLAT)
        self.endTimeLab.configure(text='''Ending Time''')

        self.stdStartLab = ttk.Label(self.timeLabFrame)
        self.stdStartLab.place(relx=0.03, rely=0.09, height=44, width=156)
        self.stdStartLab.configure(background="#d9d9d9")
        self.stdStartLab.configure(foreground="#000000")
        self.stdStartLab.configure(relief=FLAT)
        self.stdStartLab.configure(text='''Starting Time 
(dd.mm.yyyy hh:mm:ss)''')

        self.epochLab = ttk.Label(self.timeLabFrame)
        self.epochLab.place(relx=0.5, rely=0.18, height=24, width=92)
        self.epochLab.configure(background="#d9d9d9")
        self.epochLab.configure(foreground="#000000")
        self.epochLab.configure(relief=FLAT)
        self.epochLab.configure(text='''(Epoch Time)''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active',"_ana2color")])
        self.useStdCheck = ttk.Checkbutton(self.timeLabFrame)
        self.useStdCheck.place(relx=0.08, rely=0.8, relwidth=0.32, relheight=0.0
                , height=26)
        self.useStdCheck.configure(variable=Simba_support.useStdVar)
        self.useStdCheck.configure(takefocus="")
        self.useStdCheck.configure(text='''Use Standard''')
        self.useStdCheck.configure(width=121)

        self.useEpoCheck = ttk.Checkbutton(self.timeLabFrame)
        self.useEpoCheck.place(relx=0.55, rely=0.8, relwidth=0.27, relheight=0.0
                , height=26)
        self.useEpoCheck.configure(variable=Simba_support.useEpoVar)
        self.useEpoCheck.configure(takefocus="")
        self.useEpoCheck.configure(text='''Use Epoch''')
        self.useEpoCheck.configure(width=102)

        self.accessLabFrame = ttk.Labelframe(top)
        self.accessLabFrame.place(relx=0.36, rely=0.48, relheight=0.3
                , relwidth=0.59)
        self.accessLabFrame.configure(text='''Access''')
        self.accessLabFrame.configure(width=380)

        self.usernameEnt = ttk.Entry(self.accessLabFrame)
        self.usernameEnt.place(relx=0.03, rely=0.34, relheight=0.18
                , relwidth=0.41)
        self.usernameEnt.configure(textvariable=Simba_support.usernameInputVar)
        self.usernameEnt.configure(takefocus="")
        self.usernameEnt.configure(cursor="ibeam")

        self.passwordEnt = ttk.Entry(self.accessLabFrame)
        self.passwordEnt.place(relx=0.5, rely=0.34, relheight=0.18
                , relwidth=0.41)
        self.passwordEnt.configure(textvariable=Simba_support.passwordInputVar)
        self.passwordEnt.configure(takefocus="")
        self.passwordEnt.configure(cursor="ibeam")

        self.usernameLab = ttk.Label(self.accessLabFrame)
        self.usernameLab.place(relx=0.03, rely=0.14, height=24, width=70)
        self.usernameLab.configure(background="#d9d9d9")
        self.usernameLab.configure(foreground="#000000")
        self.usernameLab.configure(relief=FLAT)
        self.usernameLab.configure(text='''Username''')

        self.passwordLab = ttk.Label(self.accessLabFrame)
        self.passwordLab.place(relx=0.5, rely=0.14, height=24, width=66)
        self.passwordLab.configure(background="#d9d9d9")
        self.passwordLab.configure(foreground="#000000")
        self.passwordLab.configure(relief=FLAT)
        self.passwordLab.configure(text='''Password''')

        self.urlEnt = ttk.Entry(self.accessLabFrame)
        self.urlEnt.place(relx=0.03, rely=0.76, relheight=0.18, relwidth=0.62)
        self.urlEnt.configure(textvariable=Simba_support.urlInputVar)
        self.urlEnt.configure(takefocus="")
        self.urlEnt.configure(cursor="ibeam")

        self.urlLab = ttk.Label(self.accessLabFrame)
        self.urlLab.place(relx=0.03, rely=0.55, height=24, width=30)
        self.urlLab.configure(background="#d9d9d9")
        self.urlLab.configure(foreground="#000000")
        self.urlLab.configure(relief=FLAT)
        self.urlLab.configure(text='''URL''')

        self.getDataButton = ttk.Button(self.accessLabFrame)
        self.getDataButton.place(relx=0.68, rely=0.76, height=30, width=98)
        self.getDataButton.configure(command=Simba_support.getData)
        self.getDataButton.configure(takefocus="")
        self.getDataButton.configure(text='''Get Data''')




# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class tagListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



