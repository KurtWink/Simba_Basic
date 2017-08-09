### Simba_Basic
Simba_Basic is an early stage prototype for an industrial control system simulation and design tool.
Feel free to edit the source at your own discretion

Users are able to create their own Python Modules which are used to perform custom operations on a set of jQuery data that is loaded into the tool.
The modified jQuery data is then given a tag classified by the operations performed, and can be either saved to a local file system or be made as a HTTP POST request as a payload.

### Current Support
The default url assembly is configured primarily for the ease of GridState use. However, data can be GET/POST from any url location as long as the host follows the same REST structure.

Currently the only supported response type is JSON. Local file system imports/exports are expected to be handled in text form or any process that can be correctly loaded by the JSON python module.

Modules are expected to be revisions of the current mod template. Any number of classes can be merged into one .py module as long as it follows the description conditions. Any multithreading, streaming, additional modules(numpy) will require the user to have those packages installed. 
Please keep this in mind when using shared mods. 

### Known Issues/Bugs
Be mindful of whitespace. Due to the flexibility of user choices, whitespace and special line characters (\n) are not parsed out of the entry fields. 
If you are having issues with pulling from a service, I would suggest clearing your entries completely and verifying your information.

Do not open multiple Hosted Service/Export Windows. The tk GUI framework does not have good support for additional top level windows, and as such the rootwork is currently unstable. 
Implementing a singleton pattern could fix this issue for the additional frames.

The current socket/streaming is not using a verifying SSL handshake. I've looked into this and have tried all of the newest certificates, however I have no control over custom certs. 
Thus, for ease of not having to handle everyone's own certs, it is disabled. 

Modules need to be placed in the same directory of Simba files in order for python's import to update correctly.

### Design Structure
The GUI framework is tkInter, and was chosen because it was native; supported on the majority of operating systems, had well written documentation, and is easily automated.
Simba runs largely from two python files. One being the GUI framework file, and the other being the support module. The framework file contains all the GUI widgets, locations, labels and everything else visual. The support module contains the meat of the program, action responses that are called by commands along with variables that are inside this module. All the data loading, editing, and http processing is done there.

These unconventional choices were largely made because of the changing requirements. Typically, for the purposes of scope and clarity it is advised to have the whole GUI and it's events in one file. Those events may range from simple to complex but the process should be done in other imports while the overall organization and readability is handled in the main file.
Without a clear direction of a visual layout, as features rolled in, the GUI needed to be adjusted even if there was space initially planned ahead.
I actually automated the base visual layout because of these changes. The initial top level windows were created as barren widgets, much like sketch or diagram. As they GUI evolved, the 'meat' of the support file was reused while the visual GUI was discarded and redone from scratch with the automation changes.

Currently, there are three GUI panels
* Main Simba Frame
* Hosted Service Panel
* Export Panel

Each of these were finally gutted and merged into one class with extensions. The automation used expected each panel to be its own application so the rootwork is unstable as a result.

Internally here are things to note:
* Blanket Exception Handling:

90% of code tends to address 10% of the issues when it comes to runtime and compile time errors. Since this is mainly a conceptual program, other than specific exceptions that I outlined in methods, additional ones are caught and thrown out. I'd hope someone would not try to pull data without an internet connection and other redundant issues like these. However real programs tend to address these and at least report specific issues for every type of infringement. Simba currently does not.
* Fixed Window:

A fully polished GUI would support different resolutions and would be resizable. To avoid worrying about widgets bugging out at certain sizes, the main frame is small and locked.
* Data Deletion:

As far as Simba's functions. It's not supposed to be a database management system. It's practical to be able to send data back for storing purposes, however there is no current way to delete records from the Simba interface. Upload at your own risk
* Stress load:

From the samples I was able to pull, it took around 8 seconds simply to load data. It slightly is unresponsive during this time. I suspect a solution would be to put the process on a different thread. Or to do whatever standard practice is done for problems like this
I'm unsure if throwing 20 years or so of a stress test will make it crash, I never had enough data to test that. However, if there are issues the loading from a direct file was far faster and may provide a temporary solution.
* Undo/Redo Stack:

I did not implement this, though wanted to. It could be as simple as storing the pre operation JSON data and reverting it on the Undo/Redo Design pattern. But there are trade offs in scalability, if you were handling three years worth of data. I'm unsure how practical it would be for storage to have iterative deep copies between each function that you apply to them.
* Saving Files:

Saving to the local file system works as expected. But, in theory if you store a massive amount of JSON data in a text doc all in one line....it tends to either crash or hand for large periods of time when opening them in a file viewer. So they may be volatile to open without a better text editor beyond notepad.


### Module Uses/Assembly

In the beginning, there were specific operations I was asked to perform on the some of the sample data. 
For example, the first operation I was tasked with was to fuzz data by an arbitrary amount of that data's standard deviation. Rather simple and it looked like this. 
```python

def stdAdjustList(jObjList, val):
    '''
    :param jObjList: The jQuery list that will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :return: The edited jQuery list to pass into the next phase.
    '''
	
    return list(map(lambda x: x + (val * numpy.std(jObjList)), jObjList))


def stdAdjustPortionList(jObj, val, portion):
    '''
    :param jObj: The jQuery list that will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :param portion: Percentage of data to be edited at random
    :return: The edited jQuery list to pass into the next phase.
    '''
   
    std = numpy.std(jObj)
    for n in range(0, len(jObj) - 1):
        if float(random.random()) < (portion * .01):
            jObj[n] = jObj[n] + (std * val)
    return jObj
```
But as the data itself changed, a lot of these operations were broken or no longer had a purpose.
There was also no strict guidelines or operations that were extremely needed. Because of all this, I created a module guideline for creating custom functions to do whatever is needed in the future.

The guideline lies below:
 ![alt text](https://github.com/KurtWink/Simba_Basic/blob/master/87c91baf7fbae3636d8b8ad3728fc094.png "Guide")
 
 In order to create the a new module, please use the template as a sample and change it from there.
 1. Rename Sample Class names 
 2. Fill out sample method Name/Attribute
 3. For any possible variables needed, create a variable object(corrsponding label, default value) 
 4. In the Do method, create the operation that will be preformed on the jQuery Data
 5. Finally add the method object to the collectionContainer
 
 Here is an extended example
 ```Python
 
 
 def collectionContainer(): # This name cannot be changed
    """
    This is a container class that contains direct lists of the functions and variables that will be displayed in the GUI
    In order to have a custom class or variable be available, it must be added to these lists.
    """
    return [zeroData()]
 
 
 
 
 class zeroData():

    def __init__(self):
        self.name = "Zero Data"
        self.attribute = "Zeroed"
		self.vars = [varObject('Starting Time', ''), varObject('Ending Time','')]

    def Do(self, jQ):
        import time
        """
            :param jObj: The jQuery collection that will be edited
            :return: The zero inserted jQuery list
			This method zeros data in a subset timerange within a set of jQuery Data
        """
        epo = jQ['epocCheck']
        jObj = jQ['dataSet']

        """ 
            n is the length of the arr
            x is the value to be looking for
            in a sorted time, low is element 0 while high is n-1
        """

            
            startEpoch = self.vars[0].value
            endEpoch = self.vars[1].value
            

            def findFirst(arr, low, high, x, n):
                if high >= low:
                    mid = int(low + (high - low) / 2)
                    if ((mid == 0 or x > float(arr[mid - 1])) and float(arr[mid]) == x):
                        return mid
                    elif (x > float(arr[mid])):
                        return findFirst(arr, (mid + 1), high, x, n)
                    else:
                        return findFirst(arr, low, (mid - 1), x, n)
                return low

            def findLast(arr, low, high, x, n):

                if high >= low:
                    mid = int(low + (high - low) / 2)
                    if ((mid == (n - 1) or x < float(arr[mid + 1])) and float(arr[mid]) == x):
                        return mid
                    elif (x < float(arr[mid])):
                        return findLast(arr, low, (mid - 1), x, n)
                    else:
                        return findLast(arr, (mid + 1), high, x, n)
                return low

            ln = len(jObj['series'][0]['timestamps'])
            timeRange2 = [x for x in range(
                findFirst(jObj['series'][0]['timestamps'], 0, ln - 1, float(startEpoch), ln),
                findLast(jObj['series'][0]['timestamps'], 0, ln - 1, float(endEpoch), ln))]

            for x in timeRange2:
                jObj['series'][0]['metrics']['interval-kwh']['floatValues'][x] = 0
```
