import sys
from getBlock import *
from tkinter import *
from base64 import b64encode


class mainInterface:
    def __init__(self, master):
        self.master = master
        master.title("Test 1")

        self.labelInfo = Label(master, text="Test 2")
        self.labelInfo.pack()

        self.labelInfoUsername = Label(master, text="Username")
        self.labelInfoUsername.pack()

        self.enterboxUsername = Entry(master)
        self.enterboxUsername.pack()

        self.labelInfoPassword = Label(master, text="Password")
        self.labelInfoPassword.pack()

        self.enterboxPassword = Entry(master)
        self.enterboxPassword.pack()

        self.labelInfoStartTime = Label(master, text="Starting Time")
        self.labelInfoStartTime.pack()

        self.enterboxStartTime = Entry(master)
        self.enterboxStartTime.pack()
        self.labelInfoStartTime.focus_set()

        self.labelInfoEndTime = Label(master, text="Ending Time")
        self.labelInfoEndTime.pack()

        self.enterboxEndTime = Entry(master)
        self.enterboxEndTime.pack()
        self.enterboxEndTime.focus_set()






        def callback():
            #userAndPass = b64encode(bytes(self.enterboxUsername.get() + ':' + self.enterboxPassword.get(), "utf-8")).decode("ascii")
            print(buildURL("default_project", "code-drop-12-test"))
            print("https://in2lytics.gridstate.io/api/default_project/series/code-drop-12-test/data")
            #f = grab(userAndPass)
            #f = zeroDatabyTimerange(str(self.enterboxStartTime.get()),str(self.enterboxEndTime.get()),50,f)



        b = Button(master, text="get", width=10, command=callback)
        b.pack()



        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()



root = Tk()
my_gui = mainInterface(root)
root.mainloop()
