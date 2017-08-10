#@Kurt Winkelmann
# NRECA 2017

def collectionContainer(): # This name cannot be changed
    """
    This is a container class that contains direct lists of the functions and variables that will be displayed in the GUI
    In order to have a custom class or variable be available, it must be added to these lists.
    This is only a sample
    """
    return [sampleMethodObject(), sampleMethodObject()]



class sampleMethodObject:  # Class object name would go here
    def __init__(self):
        self.name = "Name of the operation/function that will be displayed in the GUI panel to be selected"
        self.attribute = "Name of the attribute that will be tagged and labeled to the set of query data"
        #Below is the variables that the function is expected to need. For each needed variable, add one object
        self.vars = [sampleVariableObject("Attribute Note", "Value"), sampleVariableObject("Sample 2", "Value")]
    def do(self, jQuery):
        """
        This is where the method's performing operation should be placed.
        jQuery will be the query set the operations will be preformed on
        Operations perform their instructions on the data given and should not return anything.
        Exceptions raise an InvalidValue for incorrect and unwanted data
        and will be handled in the support Module when the selected methodObject's operation is executed.
        Required variables can be found by looking at custom variables that will defined in _init_
        It should be assumed that variables will be string values and ""/null at default
        Once a custom methodObject class is made, in order to add it to the list of displayed operations,
        the entire class object will need to be placed in 'collectionContainer'
        """


class sampleVariableObject:  # Class object name would go here
    def __init__(self, name, value):
        """
        This is a custom variable, in order to add this variable to the displayed list it must be added to the catalog
        Nothing is really needed to be changed for use except for the class name for organization
        """
        self.name = name #"Name of variable that will be displayed in the GUI list"
        self.value = value #"Value as a string that will be user inputted onto the variable in the GUI, and is None until a user defines it"


