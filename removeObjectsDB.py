from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class RemoveObjectsDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Cleanup Model',
            self.OK|self.APPLY|self.CANCEL, )
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        GroupBox_1 = FXGroupBox(p=self, text='Delete', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        FXRadioButton(p=GroupBox_1, text='Suppressed Instances', tgt=form.kw_box1Kw1, sel=96)
        FXRadioButton(p=GroupBox_1, text='Unused Parts', tgt=form.kw_box1Kw1, sel=97)
        FXRadioButton(p=GroupBox_1, text='Both', tgt=form.kw_box1Kw1, sel=98)
        l = FXLabel(p=self, text='Caution - there is no Undo!', opts=JUSTIFY_LEFT)
