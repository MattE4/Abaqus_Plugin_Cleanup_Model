from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class RemoveObjects_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='delOb',
            objectName='delete_objects', registerQuery=False)
        pickedDefault = ''
        if 'kw_box1' not in self.radioButtonGroups:
            self.kw_box1Kw1 = AFXIntKeyword(None, 'kw_box1Dummy', True)
            self.kw_box1Kw2 = AFXStringKeyword(self.cmd, 'kw_box1', True)
            self.radioButtonGroups['kw_box1'] = (self.kw_box1Kw1, self.kw_box1Kw2, {})
        self.radioButtonGroups['kw_box1'][2][96] = 'Suppressed Instances'
        self.kw_box1Kw1.setValue(96)
        if 'kw_box1' not in self.radioButtonGroups:
            self.kw_box1Kw1 = AFXIntKeyword(None, 'kw_box1Dummy', True)
            self.kw_box1Kw2 = AFXStringKeyword(self.cmd, 'kw_box1', True)
            self.radioButtonGroups['kw_box1'] = (self.kw_box1Kw1, self.kw_box1Kw2, {})
        self.radioButtonGroups['kw_box1'][2][97] = 'Unused Parts'
        if 'kw_box1' not in self.radioButtonGroups:
            self.kw_box1Kw1 = AFXIntKeyword(None, 'kw_box1Dummy', True)
            self.kw_box1Kw2 = AFXStringKeyword(self.cmd, 'kw_box1', True)
            self.radioButtonGroups['kw_box1'] = (self.kw_box1Kw1, self.kw_box1Kw2, {})
        self.radioButtonGroups['kw_box1'][2][98] = 'Both'

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import removeObjectsDB
        return removeObjectsDB.RemoveObjectsDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Cleanup Model', 
    object=RemoveObjects_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import delete_objects',
    applicableModules=['Part', 'Assembly'],
    version='1.0',
    author='',
    description='Plug-In to delete suppressed instances and/or parts without any instance in the currently displayed model.'\
    			'\n\nThis is not an official Dassault Systemes product.',
    helpUrl='N/A'
)
