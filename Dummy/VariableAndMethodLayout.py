class collectionContainer():
    """
    This is a container class that contains direct lists of the functions and variables that will be displayed in the GUI
    In order to have a custom class or variable be available, it must be added to these lists.
    This is only a sample, the actual module is operationList
    """
    SampleCatalogList = [sampleMethodObject()]



class sampleMethodObject:  # Class object name would go here
    def __init__(self):
        self.name = "Name of the operation/function that will be displayed in the GUI panel to be selected"
        self.attribute = "Name of the attribute that will be taged and labeled to the set of query data"
        self.vars = [sampleVariableObject("Sample", 0)]
    def do(self, globalVarCollection):
        """
        This is where the method's performing operation should be placed.
        globalVarCollection will be the global dict of variables available to use.
        Operations perform their instructions on the data given and should not return anything.
        Exceptions raise an InvalidValue for incorrect and unwanted data
        and will be handled in the support Module when the selected methodObject's operation is executed.
        Required variables can be found by looking at the variable documentation. If a variable is not currently implemented,
        non native variables can be created, with the format below.
        Once a custom methodObject class is made, in order to add it to the list of displayed operations,
        the entire class will need to be placed in 'operationList' or imported as a separate,
        in addition to an the custom methodObject being placed in the list of operation objects.
        """


class sampleVariableObject:  # Class object name would go here
    def __init__(self, name, value):
        """
        This is a custom variable, in order to add this variable to the displayed list it must be added to the catalog
        """
        self.name = name #"Name of variable that will be displayed in the GUI list"
        self.value = value #"Value as a string that will be user inputted onto the variable in the GUI, and is None until a user defines it"

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    def getName(self, name):
        return self.name
    def setName(self,name):
        self.name = name
