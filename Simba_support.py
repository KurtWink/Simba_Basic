#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 24, 2017 07:59:36 AM


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
from base64 import b64encode
from tkinter import filedialog
from tkinter import messagebox
import json
import requests
import time
import importlib
def set_Tk_var():
    # Vars for Main Frsmr
    global combobox
    combobox = StringVar()
    global loadBarVar
    loadBarVar = IntVar()
    loadBarVar.set(0)
    global epocCheck
    global dataSet
    dataSet = None
    epocCheck = None
    global operationSet
    global varsAndFunc
    global localInputPathVar
    localInputPathVar = StringVar()
    global editVarVar
    editVarVar = StringVar()


    #Vars for HostedService
    global projectInputVar
    projectInputVar = StringVar()
    global seriesInputVar
    seriesInputVar = StringVar()
    global stdStartVar
    stdStartVar = StringVar()
    global epoStartVar
    epoStartVar = StringVar()
    global stdEndVar
    stdEndVar = StringVar()
    global epoEndVar
    epoEndVar = StringVar()
    global useStdVar
    useStdVar = StringVar()
    global useEpoVar
    useEpoVar = StringVar()
    global usernameInputVar
    usernameInputVar = StringVar()
    global passwordInputVar
    passwordInputVar = StringVar()
    global urlInputVar
    urlInputVar = StringVar()

    #Vars for Export Frame
    global usernameOutVar
    usernameOutVar = StringVar()
    global passwordOutVar
    passwordOutVar = StringVar()
    global projectOutVar
    projectOutVar = StringVar()
    global urlOutVar
    urlOutVar = StringVar()
    global nameChangeVar
    nameChangeVar = StringVar()
#Methods for the Main Frame

def getEditVar():
    return editVarVar.get()

def doSelectedOps(var):

    for x in var:
        try:
            globals()['varsAndFunc'][x].functionX(globals())
            globals()['dataSet']['series'][0]['tags'][globals()['varsAndFunc'][x].name] = "1"
        except ValueError:
            messagebox.showerror("Error",
                                 "There is no data set loaded or an invalid range of values have been selected\nPlease review your dataset options")

def clearData():
    print('Simba_support.clearData')
    sys.stdout.flush()

def getLocalData():
    file = filedialog.askopenfile(mode='a')
    x_file = open(file.name)

    globals()['dataSet'] = json.loads(x_file.read())
    if ('error' in globals()['dataSet']) or (globals()['dataSet'] == {}):
        globals()["dataSet"] = None
        globals()["loadBarVar"].set(0)
        raise ValueError
    else:
        globals()['loadBarVar'].set(100)
    x_file.close()

def loadMod():
    place = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if place is not None:
        name = place[place.rfind('/'):]
        name = name[1:]
        name = name[:len(name)-3]
        module = importlib.import_module((name))
        importlib.invalidate_caches()
        global varsAndFunc
        varsAndFunc = getattr(module, 'collectionContainer')

def checkVal():
    print(varsAndFunc()[0].vars[0].value)


def getMod():
    return varsAndFunc
def openHelp():
    print('Simba_support.openHelp')
    sys.stdout.flush()

def saveLocalData():
    print('Simba_support.saveLocalData')
    sys.stdout.flush()
#Methods for Export
def buildUrlOut():
    return "https://in2lytics.gridstate.io/api/" + projectOutVar.get() + "/series/"

def pushDataSet():
    url = buildUrlOut()
    auth = b64encode(bytes(usernameOutVar.get() + ':' + passwordOutVar.get(), "utf-8")).decode("ascii")
    if not (nameChangeVar.get() == "" or nameChangeVar.get() is None):
        dataSet['series'][0]['tags']['file-name'] = nameChangeVar.get()
    headers = {'Authorization': 'Basic %s' % auth}
    response = requests.request("POST", url, headers=headers, json=globals()['dataSet'], verify=False)
    return response
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
#Methods for  Hosted Service
def buildURL():
    return "https://in2lytics.gridstate.io/api/" + projectInputVar.get() + "/series/" + seriesInputVar.get() + "/data"
def getJsonSet(auth, url):

    if epocCheck is None:
        raise ValueError()
    if epocCheck:
        startEpoch = globals()['startTimeEpoVar'].get()
        endEpoch = globals()['endingTimeEpoVar'].get()
    else:
        pattern = '%d.%m.%Y %H:%M:%S'
        startEpoch = int(
            time.mktime(time.strptime(globals()['startingTimeStdVar'].get(), pattern))) * 1000
        endEpoch = int(
            time.mktime(time.strptime(globals()['endingTimeStdVar'].get(), pattern))) * 1000

    querystring = {"start_time": ""+str(startEpoch), "end_time": ""+str(endEpoch)}
    print(querystring)
    headers = {'Authorization': 'Basic %s' % auth}

    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    return json.loads(response.text)
def getData():
    url = urlInputVar.get()
    userAndPass = b64encode(bytes(usernameInputVar.get() + ':' + passwordInputVar.get(), "utf-8")).decode("ascii")
    globals()['dataSet'] = getJsonSet(userAndPass, url)
    print(globals()['dataSet'])
    if ('error' in globals()['dataSet']) or (globals()['dataSet'] == {}):
        globals()["dataSet"] = None
        globals()["loadVar"].set(0)
        raise ValueError
    else:
        globals()['loadVar'].set(100)
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import Simba
    Simba.vp_start_gui()


