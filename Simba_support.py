#! /usr/bin/env python
#
# Support module frame was generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 24, 2017 07:59:36 AM



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
import importlib
import json
import time
from tkinter import simpledialog
from base64 import b64encode
from tkinter import filedialog
from tkinter import messagebox



import requests


def set_Tk_var():
    '''
    Sets global vars for the support file
    :return:
    '''
    # Vars for Main Frsmr
    global combobox
    combobox = StringVar()
    global loadBarVar
    loadBarVar = IntVar()
    loadBarVar.set(0)

    global dataSet
    dataSet = None

    global operationSet
    global varsAndFunc
    global localInputPathVar
    localInputPathVar = StringVar()
    global editVarVar
    editVarVar = StringVar()
    # Strange GUI triggers
    global enableLoadVar
    enableLoadVar = False

    # Vars for HostedService
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
    global epoCheck
    epoCheck = None
    global usernameInputVar
    usernameInputVar = StringVar()
    global passwordInputVar
    passwordInputVar = StringVar()
    global urlInputVar
    urlInputVar = StringVar()

    # Vars for Export Frame
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


# Methods for the Main Frame

def getEditVar():
    return editVarVar.get()


def doSelectedOps(var):
    '''
    Function takes the currently selected method object and does their corrosponding function
    Label is then applied to the dataset and is asked to be named by a simple prompt
    Any additional exception handling for future custom functions should be added here. The value error is a broad catch
    :param var: The currently Selected Method Object
    :return:
    '''


    try:
        globals()['varsAndFunc'][var].do(globals()['dataSet'])
        val = simpledialog.askstring("Addtional Tag Value:", "Please Provide An Tag Value")
        globals()['dataSet']['series'][0]['tags'][globals()['varsAndFunc'][var].attribute] = val
    except ValueError:
        messagebox.showerror("Error",
                             "There is no data set loaded or an invalid input of variables have been made\nPlease review your dataset options")


def clearData():
    '''
    Clears the currently loaded data set and reflects the changes in the GUI
    :return:
    '''
    globals()["dataSet"] = None
    globals()['enableLoadVar'] = False
    globals()["loadBarVar"].set(0)


def getLocalData():
    '''
    Function opens a file prompt asking for local file path
    File is then loaded into json format and should raise errors if incorrectly assembled
    :return:
    '''
    file = filedialog.askopenfile(mode='a')
    x_file = open(file.name)
    try:
        globals()['dataSet'] = json.loads(x_file.read())
    except:
        messagebox.showerror("Error",
                             "This dats is not JSON or contains errors")
    if ('error' in globals()['dataSet']) or (globals()['dataSet'] == {}):
        globals()["dataSet"] = None
        globals()["loadBarVar"].set(0)
        raise ValueError
    else:
        globals()['loadBarVar'].set(100)
        globals()['enableLoadVar'] = True
    x_file.close()


def loadMod():
    '''
    Function asks for a file location name. Due to the module imports, the file must be in the same directory as the
    Simba files
    :return:
    '''
    place = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if place is not None:
        name = place[place.rfind('/'):]
        name = name[1:]
        name = name[:len(name) - 3]
        module = importlib.import_module((name))
        importlib.invalidate_caches()
        global varsAndFunc
        varsAndFunc = getattr(module, 'collectionContainer')()


def getMod():
    '''
    Getter for modlist
    :return: list of methodObjects
    '''
    return varsAndFunc


def openHelp():
    pass


def saveLocalData():
    '''
    Writes the currently held jQuery Set to the file location through a dialog prompt
    Lazy Exception handling due to most serious File I/O exceptions being handled by the native dialog
    :return:
    '''
    try:
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        # open(filedialog.asksaveasfilename(filetypes=[("Text ", "*.txt")]), 'w')
        file.write(json.dumps(dataSet))
        file.close()
    except:
        pass


# Methods for Export

def buildUrlOut():
    '''
    Builds the native gridstate.io output url from the output directory entry in the GUI
    :return: String (url value)
    '''
    return "https://in2lytics.gridstate.io/api/" + projectOutVar.get() + "/series/"


def pushDataSet():
    '''
    Function sends a http get request to push data onto a hosated service
    The auth is implied to be basic/simple username and password
    If a name change is used, then the data will be placed in a new series under that name (assuming the restAPI works)
    :return:
    '''
    url = urlOutVar.get()
    auth = b64encode(bytes(usernameOutVar.get() + ':' + passwordOutVar.get(), "utf-8")).decode("ascii")
    if not (nameChangeVar.get() == "" or nameChangeVar.get() is None):
        dataSet['series'][0]['tags']['file-name'] = nameChangeVar.get()
    headers = {'Authorization': 'Basic %s' % auth}
    response = requests.request("POST", url, headers=headers, json=globals()['dataSet'], verify=False)
    return response


def init(top, gui, *args, **kwargs):
    '''
    Init root setup
    :param top:
    :param gui:
    :param args: None currently handled
    :param kwargs: None currently handled
    :return:
    '''
    global w, top_level, root
    w = gui
    top_level = top
    root = top


# Methods for  Hosted Service
def epochTime():
    '''
    Sets a timecheck variable for when epoch time is being used (These both don't really need to be methods)
    :return:
    '''
    globals()['epoCheck'] = True


def standardTime():
    '''
    Sets a timecheck variable for when standard time is being used
    :return:
    '''
    globals()['epoCheck'] = False


def buildURL():
    '''
    Builds native gridstate url from GUI project and series entries
    :return: String (url Value)
    '''
    return "https://in2lytics.gridstate.io/api/" + projectInputVar.get() + "/series/" + seriesInputVar.get() + "/data"


def getJsonSet(auth, url):
    '''
    Function handles timequery and http requests
    Currently looking need streaming, secure requests
    :param auth: String (The simple auth provided by encoded info (should expand later))
    :param url: String
    :return:
    '''
    if (epoCheck is None):
        raise ValueError()
    if epoCheck:
        startEpoch = globals()['epoStartVar'].get()
        endEpoch = globals()['epoEndVar'].get()
    else:
        try:
            pattern = '%d.%m.%Y %H:%M:%S'
            startEpoch = int(
                time.mktime(time.strptime(globals()['stdStartVar'].get(), pattern))) * 1000
            endEpoch = int(
                time.mktime(time.strptime(globals()['stdEndVar'].get(), pattern))) * 1000
        except:
            raise ValueError()

    querystring = {"start_time": "" + str(startEpoch), "end_time": "" + str(endEpoch)}
    headers = {'Authorization': 'Basic %s' % auth}
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    return json.loads(response.text)


def getData():
    '''
    Loads and assigns jQuery from simple username and password auth to a variable.
    Raises Value errors on failing to load data, should be handled accordingly
    Visually sets the loadbar graphic in the GUI if the data is received correctly
    :return:
    '''
    url = urlInputVar.get()
    userAndPass = b64encode(bytes(usernameInputVar.get() + ':' + passwordInputVar.get(), "utf-8")).decode("ascii")
    globals()['dataSet'] = getJsonSet(userAndPass, url)
    if ('error' in globals()['dataSet']) or (globals()['dataSet'] == {}):
        globals()["dataSet"] = None
        globals()["loadBarVar"].set(0)
        raise ValueError
    else:
        globals()['loadBarVar'].set(100)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import Simba

    Simba.vp_start_gui()
