from __future__ import absolute_import, division
from psychopy import locale_setup, core, gui, data#, event#, logging#, visual
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
                                
# Make sure that under Psychopy preferences, under audio library pygame is listed first.                     
# Make sure the bottem dialog bar auto hides
                      
# DIALOG BOX RESOURCES
# http://www.blog.pythonlibrary.org/2010/07/10/the-dialogs-of-wxpython-part-2-of-2/
# Clock resources: psychopy-users/tFghyXkOx5U
#from psychopy.gui import wxgui

import os  # handy system and path functions
import sys  # to get file system encoding
import wx
import numpy as np
import glob
sys.path.insert(0, '../DataHandlingScripts')
import CheckExistingNeuroPsychData

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))#.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from NCM_NeuroPsych_Config import *
# Check to see if the output data folder has been identified
try:
    # try to load the config file
    from NeuropsychDataFolder import *
    # See if the variable is in it
    print('Data being saved to: %s'%(NeuropsychDataFolder))
    if not os.path.exists(NeuropsychDataFolder):
        raise ValueError('Folder does not exist.')
        
except:
    app = wx.App()
    dlg = wx.DirDialog(None, "Choose data output directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
    if dlg.ShowModal() == wx.ID_OK:
        print(dlg.GetPath())
    OutFolder = dlg.GetPath()
    dlg.Destroy()    
    # write the selected folder to the config file
    fid = open(os.path.join(_thisDir, '..','ConfigFiles','NeuropsychDataFolder.py'),'w')
    fid.write('NeuropsychDataFolder = \'%s\''%(OutFolder))
    fid.close()
    NeuropsychDataFolder = OutFolder
    


Top = 20
Left = 20
RowWidth = 50
ColWidth = 100
# Button height cannot be changed
ButtonHeight = -1
ButtonWidth = 85
LabelOffset = 10
# Allow flexible number of rows
NRows =  12
# Create a list of what pixel each row is to be set to
RowPixel = []
for i in range(NRows):
    RowPixel.append(Top + i*RowWidth)
# Allow flexible number of columns
NCols =  7
# Create a list of what pixel each row is to be set to
ColPixel = []
for i in range(NCols):
    ColPixel.append(Top + i*ColWidth)

NColForBox = 7
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      print('Got here 3')
      super(Mywin, self).__init__(parent, title = title,size = (800,600))  
      self.panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      
      
      self.DataFolder = NeuropsychDataFolder
      print(NeuropsychDataFolder)
      if not os.path.exists(self.DataFolder):
        # If my specified folder does not exist, then put the data up two folders.
            self.DataFolder = "../../data"
            if not os.path.exists(self.DataFolder):
                os.mkdir(self.DataFolder)
      
      self.VisitFolderPath = 'empty'
      # Setup the Participant ID entry
      self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Participant ID:", pos = (ColPixel[0],RowPixel[0]))
      self.PartID = wx.TextCtrl(self.panel,-1,'9999999',size=(ButtonWidth,-1),pos = (ColPixel[1],RowPixel[0]))
      self.btnPartEntry = wx.Button(self.panel,-1,label = "Submit", pos = (ColPixel[2],RowPixel[0]), size = ((ButtonWidth, ButtonHeight))) 
      self.btnPartEntry.Bind(wx.EVT_BUTTON, self.OnCickPartEntry)
      self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Output folder:" , pos = (ColPixel[3],RowPixel[0]))
        
      # Create Default values for the load levels for the two tasks
      self.FRTBlockLoadLevels = '0.0 0.125 0.25 0.375 0.5'
      self.DMSBlockLoadLevels = '1 3 5 6 7'
      self.VSTMBlockLoadLevels = '1 2 3 4 5'     
      self.DMSFontSize = '60'
      self.DMSTag = 0
      self.VSTMTag = 0
      self.NBackTag = 0
      self.VSTMCapacity = 4
      self.DMSCapacity = 5
      # ###################
      CurrentRow = RowPixel[2]
#      # #### Row 3
      self.titleR3 = wx.StaticText(self.panel, -1, label = "Spatial/Dots", pos = (ColPixel[0]+LabelOffset/2,CurrentRow+LabelOffset))
#      # Buttons
      self.btnR3C1 = wx.Button(self.panel,-1,"Instructions", pos = (ColPixel[1],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C1.Bind(wx.EVT_BUTTON,self.OnClickedR3C1)        
#      self.btnR3C2 = wx.Button(self.panel,-1,"Demo", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
#      self.btnR3C2.Bind(wx.EVT_BUTTON,self.OnClickedR3C2) 
#      self.btnR3C3 = wx.Button(self.panel,-1,"Stair", pos = (Col3,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
#      self.btnR3C3.Bind(wx.EVT_BUTTON,self.OnClickedR3C3) 
      self.btnR3C3 = wx.Button(self.panel,-1,"Block1", pos = (ColPixel[5],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C3.Bind(wx.EVT_BUTTON,self.OnClickedR3C3) 
      
      self.btnR3C4 = wx.Button(self.panel,-1,"Block2", pos = (ColPixel[6],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C4.Bind(wx.EVT_BUTTON,self.OnClickedR3C4) 
      
      # Text box for the capacity value
      self.txtR3C4 = wx.StaticText(self.panel, -1, label = "Cap =", pos = (ColPixel[3]+5,CurrentRow+LabelOffset))
      self.txtR3C5 = wx.StaticText(self.panel, -1, label = "000", pos = (ColPixel[4]-ColWidth/2+5,CurrentRow+LabelOffset))  
      self.btnR3C5a = wx.Button(self.panel,-1,"Enter", pos = (ColPixel[4]-5,CurrentRow), size = ((ButtonWidth/2+5, ButtonHeight))) 
      self.btnR3C5b = wx.Button(self.panel,-1,"Load", pos = (ColPixel[4]+40,CurrentRow), size = ((ButtonWidth/2+5, ButtonHeight))) 
      self.btnR3C5a.Bind(wx.EVT_BUTTON, self.OnClickedVSTMCapEnter)
      self.btnR3C5b.Bind(wx.EVT_BUTTON, self.LoadVSTMCapacity)
      
      # Make a box around the Capacity text and entry buttons
      Row3BoxR5 = wx.StaticBox(self.panel, -1, size = ((ColWidth*2),RowWidth-5), pos = (ColPixel[3],CurrentRow-5))

#      # Box
      Row1BoxR3 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (ColPixel[0],CurrentRow-5))
      # Checkboxes
 #     self.cbR3C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
 #     self.cbR3C3 = wx.CheckBox(self.panel, -1, label = "", pos = (Col3 + ButtonWidth+5,CurrentRow))
      self.cbR3C3 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[5] + ButtonWidth-3,CurrentRow))
      self.cbR3C4 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[6] + ButtonWidth-3,CurrentRow))
# ###################
      CurrentRow = RowPixel[3]
#      # #### Row 3
      self.titleR5 = wx.StaticText(self.panel, -1, label = "DMS/Letters", pos = (ColPixel[0]+LabelOffset/2,CurrentRow+LabelOffset))
#      # Buttons
      self.btnR5C1 = wx.Button(self.panel,-1,"Instructions", pos = (ColPixel[1],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C1.Bind(wx.EVT_BUTTON,self.OnClickedR5C1)        
#     self.btnR5C2 = wx.Button(self.panel,-1,"Demo", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
 #     self.btnR5C2.Bind(wx.EVT_BUTTON,self.OnClickedR5C2) 
 #     self.btnR5C3 = wx.Button(self.panel,-1,"Stair", pos = (Col3,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
 #     self.btnR5C3.Bind(wx.EVT_BUTTON,self.OnClickedR5C3) 
      # Text box for the capacity value
      self.txtR5C4 = wx.StaticText(self.panel, -1, label = "Cap =", pos = (ColPixel[3]+5,CurrentRow+LabelOffset))
      self.txtR5C5 = wx.StaticText(self.panel, -1, label = "000", pos = (ColPixel[4]-ColWidth/2+5,CurrentRow+LabelOffset))  
      self.btnR5C5a = wx.Button(self.panel,-1,"Enter", pos = (ColPixel[4]-5,CurrentRow), size = ((ButtonWidth/2+5, ButtonHeight))) 
      self.btnR5C5b = wx.Button(self.panel,-1,"Load", pos = (ColPixel[4]+40,CurrentRow), size = ((ButtonWidth/2+5, ButtonHeight))) 
      self.btnR5C5a.Bind(wx.EVT_BUTTON, self.OnClickedDMSCapEnter)
      self.btnR5C5b.Bind(wx.EVT_BUTTON, self.LoadDMSCapacity)
      # Make a box around the Capacity text and entry buttons
      Row5BoxR5 = wx.StaticBox(self.panel, -1, size = ((ColWidth*2),RowWidth-5), pos = (ColPixel[3],CurrentRow-5))
      
      self.btnR5C6 = wx.Button(self.panel,-1,"Block1", pos = (ColPixel[5],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C6.Bind(wx.EVT_BUTTON,self.OnClickedR5C6) 
      self.btnR5C7 = wx.Button(self.panel,-1,"Block2", pos = (ColPixel[6],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C7.Bind(wx.EVT_BUTTON,self.OnClickedR5C7) 
#     
# Box
      Row1BoxR5 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (ColPixel[0],CurrentRow-5))
      # Checkboxes
 #     self.cbR5C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
 #     self.cbR5C3 = wx.CheckBox(self.panel, -1, label = "", pos = (Col3 + ButtonWidth+5,CurrentRow))
      self.cbR5C6 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[5] + ButtonWidth-3,CurrentRow))
      self.cbR5C7 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[6] + ButtonWidth-3,CurrentRow))

# #### N-BACK #########
      CurrentRow = RowPixel[4]
#      # #### Row 3
      self.titleR5 = wx.StaticText(self.panel, -1, label = "N-Back", pos = (ColPixel[0]+LabelOffset/2,CurrentRow+LabelOffset))
#      # Buttons
      self.btnR10C1 = wx.Button(self.panel,-1,"Instructions", pos = (ColPixel[1],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR10C1.Bind(wx.EVT_BUTTON,self.OnClickedR10C1)             
      
    #  self.btnR10C3 = wx.Button(self.panel,-1,"Practice", pos = (ColPixel[2],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
    #  self.btnR10C3.Bind(wx.EVT_BUTTON,self.OnClickedR10C3)
      
      self.btnR10C3 = wx.Button(self.panel,-1,"Block1", pos = (ColPixel[5],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR10C3.Bind(wx.EVT_BUTTON,self.OnClickedR10C3)
      
      self.btnR10C4 = wx.Button(self.panel,-1,"Block2", pos = (ColPixel[6],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR10C4.Bind(wx.EVT_BUTTON,self.OnClickedR10C4)
      # Checkboxes
      #self.cbR10C3 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[2] + ButtonWidth+5,CurrentRow))      
      self.cbR10C3 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[5] + ButtonWidth-3,CurrentRow))      
      self.cbR10C4 = wx.CheckBox(self.panel, -1, label = "", pos = (ColPixel[6] + ButtonWidth-3,CurrentRow))      
      # Box around buttons
      Row1BoxR10 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (ColPixel[0],CurrentRow-5))

      
      
      self.btnClose = wx.Button(self.panel,-1,"Close", pos = (ColPixel[0],RowPixel[9]), size = ((ButtonWidth, ButtonHeight))) 
      self.btnClose.Bind(wx.EVT_BUTTON,self.CloseGUI) 
      
      self.Centre() 
      self.Show() 
      self.Fit()  
      
   def DisableAll(self): 
      for child in self.panel.GetChildren():
        # Diable all buttons except the button to enter the participant ID
        if isinstance(child, wx.Button):
            if child.Label != "Submit":
                child.Disable()
   
   def EnableAll(self): 
      for child in self.panel.GetChildren():
        # Diable all buttons except the button to enter the participant ID
        if isinstance(child, wx.Button):
            if (child.Label != "Submit"):
                child.Enable()
            if (child.Label == "Paper Folding"):
                child.Disable()
    
   def CheckAvailableData(self):
        # This needs to check off the data that has been collected already
        for i in self.CurrentData.TaskList:
            if self.CurrentData.TaskList[i]['Completed'] == True:
                print(self.CurrentData.TaskList[i])
                try:
                    exec('self.%s.SetValue(True)'%(self.CurrentData.TaskList[i]['CBLoc']))      
                except:
                    pass
    
   def LoadVSTMCapacity(self, event):
        expName = 'VSTM'
        Tag = '1'
        CapacityFileName = os.path.join(self.VisitFolderPath, '%s_%s_%s_%s_%s.csv' % (self.PartID.GetValue(), expName, 'CAPACITY', Tag, '*'))
        # Find the capacity file and only select the last one if there are more than one
        CapacityFileName = glob.glob(CapacityFileName)[-1]
        # Now open and read the file
        file = open(CapacityFileName, 'r')
        self.VSTMCapacity = file.read()
        self.txtR3C5.SetLabelText(self.VSTMCapacity)
        # close the file
        file.close()
        self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMCapacity)
        
   def LoadDMSCapacity(self,event):
        expName = 'DMS'
        Tag = '1'
        CapacityFileName = os.path.join(self.VisitFolderPath, '%s_%s_%s_%s_%s.txt' % (self.PartID.GetValue(), expName, 'CAPACITY', Tag, '*'))
        # Find the capacity file and only select the last one if there are more than one
        CapacityFileName = glob.glob(CapacityFileName)[-1]
        # Now open and read the file
        file = open(CapacityFileName, 'r')
        self.DMSCapacity = file.read()
        self.txtR5C5.SetLabelText(self.DMSCapacity)
        # close the file
        file.close()
        self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSCapacity)

   def OnClickedR6C2(self, event):
    pass


    
   def ManualEntryCapacity(self,Range):
        myDlg = gui.Dlg(title=u"NCM Lab", labelButtonOK=' OK ', labelButtonCancel=' Cancel ',)
        myDlg.addField(u'Capacity:')
        myDlg.show()  # show dialog and wait for OK or Cancel
        Capacity = -9999
        if myDlg.OK:  # then the user pressed OK
            thisInfo = myDlg.data
    
            if (float(thisInfo[0]) >= float(Range[0])) and (float(thisInfo[0]) <= float(Range[1])):
                print("Capacity = " + str(thisInfo))
                Capacity = float(thisInfo[0])
            else:
                print("Out of Range")
        else:
            print("user cancelled")
        return str(Capacity)
        
   def OnClickedVSTMCapEnter(self,event):
        self.VSTMCapacity = self.ManualEntryCapacity([0.0, 36])
        self.txtR3C5.SetLabelText(self.VSTMCapacity)
        self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMCapacity)

   def OnClickedDMSCapEnter(self,event):
        self.DMSCapacity = self.ManualEntryCapacity([0.0, 9])
        self.txtR5C5.SetLabelText(self.DMSCapacity)
        self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSCapacity)

   def CreateVSTMList5(self, VSTMCapacity):
        Limit = int(round(float(VSTMCapacity) + 1))
        if Limit > 15:
            Limit = 15
        elif Limit < 5:
            Limit = 5
        VSTMList = {}
        VSTMList['5']=[1,2,3,4,5]
        VSTMList['6']=[1,3,4,5,6]
        VSTMList['7']=[1,3,5,6,7]
        VSTMList['8']=[1,3,6,7,8]
        VSTMList['9']=[1,3,6,8,9]    
        VSTMList['10']=[1,3,6,9,10]    
        VSTMList['11']=[1,3,6,11,12]    
        VSTMList['12']=[1,3,6,12,13]    
        VSTMList['13']=[1,3,6,13,14]    
        VSTMList['14']=[1,3,6,14,15]    
        VSTMList['15']=[1,3,6,15,16]    
        OutList = VSTMList[str(Limit)]
        OutList = ' '.join(str(e) for e in OutList)
        return OutList   
   
   def CreateDMSList6(self, DMSCapacity):
        Limit = int(round(float(DMSCapacity) + 1))
        if Limit > 9:
            Limit = 9
        elif Limit < 6:
            Limit = 6
        DMSList = {}
        DMSList['6']=[1,2,3,4,5,6]
        DMSList['7']=[1,2,3,5,6,7]
        DMSList['8']=[1,2,4,5,7,8]
        DMSList['9']=[1,2,4,6,8,9]    
        OutList = DMSList[str(Limit)]
        OutList = ' '.join(str(e) for e in OutList)
        return OutList
   
   def CreateDMSList5(self, DMSCapacity):
        Limit = int(round(float(DMSCapacity) + 1))
        if Limit > 9:
            Limit = 9
        elif Limit < 6:
            Limit = 6
        DMSList = {}
        DMSList['6']=[1,3,4,5,6]
        DMSList['7']=[1,3,5,6,7]
        DMSList['8']=[1,3,6,7,8]
        DMSList['9']=[1,3,6,8,9]    
        OutList = DMSList[str(Limit)]
        OutList = ' '.join(str(e) for e in OutList)
        return OutList
   
   def CheckPartFolder(self):
      PartFolder = os.path.join(self.DataFolder,self.PartID.GetValue())
      # Does the part folder for data exist?
      PartFolderFlag = False
      PartFolderFlag = os.path.exists(PartFolder)
      
      print(PartFolderFlag)
      if PartFolderFlag:
        self.PartFolder = PartFolder
        print('Participant Folder Exists: %s'%(self.PartFolder))
      else:
        self.PartFolder = PartFolder
        print('Participant Folder Does Not Exists')
        self.CreatePartFolder()
      
   def CheckVisitFolder(self):
        # What folders are in the Part folder?
        ListOfVisitFolders = []
        ListOfVisitFoldersNames = [];
        for root, dirs, files in os.walk(self.PartFolder, topdown=False):
            for name in dirs:
                print(name)
                ListOfVisitFolders.append(int(name[-1]))
                ListOfVisitFoldersNames.append(name)
        
        print(ListOfVisitFolders)
        if len(ListOfVisitFolders) == 0:
            # No visit folder yet, make one with a name of V001
            self.VisitFolderName = '%s_V00%d'%(data.getDateStr(), 1)
            self.VisitFolderPath = os.path.join(self.PartFolder,self.VisitFolderName)
            os.mkdir(self.VisitFolderPath)
            
        else:
            # Visit folder exists. 
            # Would you like to use the same one?
            dlg = wx.MessageDialog(self, 'A Visit folder(s) already exist for this participant, would you like to use it?','', wx.YES_NO | wx.CANCEL | wx.ICON_ERROR)
            dlg.Show()
            if dlg.ShowModal() == wx.ID_YES: # Note, this is how you get the yes responses
                # If the user wants to restart a visit then have them select the visit to reuse
                dlg = wx.SingleChoiceDialog(self, 'Select a visit','Select Visit Folder', ListOfVisitFoldersNames,wx.CHOICEDLG_STYLE)
                dlg.Show()
                if dlg.ShowModal() == wx.ID_OK:
                    print('You selected: %s\n' % dlg.GetStringSelection())
                    self.VisitFolderName = dlg.GetStringSelection()
                    self.VisitFolderPath = os.path.join(self.PartFolder, self.VisitFolderName)
                dlg.Destroy()
                
                # If the visit folder exists, load the data in it and see what it has
                self.CurrentData = CheckExistingNeuroPsychData.NeuroPsychData(self.VisitFolderPath)
                #self.CheckAvailableData()
                
            else:
                # Make a new visit
                # New visit folders will increment the visit number V002, V003, etc
                self.VisitFolderName = '%s_V00%d'%(data.getDateStr(),ListOfVisitFolders[-1]+1)
                self.VisitFolderPath = os.path.join(self.PartFolder,self.VisitFolderName)
                os.mkdir(self.VisitFolderPath)
        print(self.VisitFolderPath)
        
        # Add the path name to the GUI
        self.PartIDLabel.SetLabelText("Output folder: %s"%(self.VisitFolderName))

   def OnCickPartEntry(self, event):
      btnName = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnName))
      # Check to see if there is a participant folder for this person
      # Need to clear the filename box and uncheck all CBs
      self.CheckPartFolder()
      self.CheckVisitFolder()
      # Enabale the buttons again
      self.EnableAll()   
   
   def CreatePartFolder(self):
      os.mkdir(self.PartFolder)

   # Row 3 Functions   
   def OnClickedR3C1(self, event):
      btnR3C1Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C1Label))
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTMInstruct.py"])   
      
   def OnClickedR3C3(self, event): 
      self.VSTMTag = self.VSTMTag + 1
      btnR3C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C3Label))
      self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMCapacity)
      print('With a capacity of %0.1f, the load levels will be:'%(float(self.VSTMCapacity)))
      print( self.VSTMBlockLoadLevels)
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTM_PassConfigFile.py", self.PartID.GetValue(), self.VisitFolderPath, self.VSTMBlockLoadLevels, 'MRIRun%d'%(self.VSTMTag),'VSTM_fMRI_Config'])  
      self.cbR3C3.SetValue(True)  
      
   def OnClickedR3C4(self, event): 
      self.VSTMTag = self.VSTMTag + 1
      btnR3C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C4Label))
      self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMCapacity)
      print('With a capacity of %0.1f, the load levels will be:'%(float(self.VSTMCapacity)))
      print( self.VSTMBlockLoadLevels)
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTM_PassConfigFile.py", self.PartID.GetValue(), self.VisitFolderPath, self.VSTMBlockLoadLevels, 'MRIRun%d'%(self.VSTMTag),'VSTM_fMRI_Config'])  
      self.cbR3C4.SetValue(True)  
   
   def OnClickedR5C1(self, event):
      btnR5C1Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C1Label))
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMSInstruct.py"])
   
      
   def OnClickedR5C6(self, event): 
      # Use the tag to keep track of the run number
      self.DMSTag = self.DMSTag + 1
      btnR5C6Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C6Label))
      self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSCapacity)
      print('With a capacity of %0.1f, the load levels will be:'%(float(self.DMSCapacity)))
      print( self.DMSBlockLoadLevels)
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMS_Adaptive5Load_v4_FMRI.py", self.PartID.GetValue(), self.VisitFolderPath, self.DMSBlockLoadLevels, self.DMSFontSize, 'MRIRun%d'%(self.DMSTag)])  
      self.cbR5C6.SetValue(True)  

   def OnClickedR5C7(self, event): 
      # Use the tag to keep track of the run number
      self.DMSTag = self.DMSTag + 1
      btnR5C7Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C7Label))
      self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSCapacity)
      print('With a capacity of %0.1f, the load levels will be:'%(float(self.DMSCapacity)))
      print( self.DMSBlockLoadLevels)
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMS_Adaptive5Load_v4_FMRI.py", self.PartID.GetValue(), self.VisitFolderPath, self.DMSBlockLoadLevels, self.DMSFontSize, 'MRIRun%d'%(self.DMSTag)])  
      self.cbR5C7.SetValue(True)  
      
   def OnClickedR10C1(self, event):
      btnR10C1Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR10C1Label))
      core.shellCall([sys.executable, "../NBack/NBackInstruct.py"])  
      
   def OnClickedR10C3(self, event):
      self.NBackTag = self.NBackTag + 1
      btnR10C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = NBack: %s"%(btnR10C3Label))
      core.shellCall([sys.executable, "../NBack/NBackPassConfigFile.py", self.PartID.GetValue(), self.VisitFolderPath, 'MRIRun%d'%(self.NBackTag), 'NBack_fMRI_Config'])  
      self.cbR10C3.SetValue(True)  
   
   def OnClickedR10C4(self, event):
      self.NBackTag = self.NBackTag + 1
      btnR10C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = NBack: %s"%(btnR10C4Label))
      core.shellCall([sys.executable, "../NBack/NBackPassConfigFile.py", self.PartID.GetValue(), self.VisitFolderPath, 'MRIRun%d'%(self.NBackTag), 'NBack_fMRI_Config'])  
      self.cbR10C4.SetValue(True)  
   
   def CloseGUI(self,event):
        self.Close()

print('Got Here 1')
app = wx.App() 
print('Got Here 2')
# Create the GUI
MyGui = Mywin(None,  'NCM Lab') 
# Disable all the buttons except teh Part ID entry 
MyGui.DisableAll()
app.MainLoop()