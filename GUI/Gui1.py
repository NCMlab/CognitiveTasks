from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
                                
                                
# DIALOG BOX RESOURCES
# http://www.blog.pythonlibrary.org/2010/07/10/the-dialogs-of-wxpython-part-2-of-2/

import os  # handy system and path functions
import sys  # to get file system encoding
import wx
import numpy as np
Top = 20
Left = 20
RowWidth = 50
ColWidth = 100
# Button height cannot be changed
ButtonHeight = -1
ButtonWidth = 80
LabelOffset = 10
Row1 = Top 
Row2 = Top + RowWidth
Row3 = Top + 2*RowWidth
Row4 = Top + 3*RowWidth
Row5 = Top + 4*RowWidth
Row6 = Top + 5*RowWidth
Row7 = Top + 6*RowWidth
Row8 = Top + 7*RowWidth

Col1 = Left
Col2 = Left + ColWidth
Col3 = Left + 2*ColWidth
Col4 = Left + 3*ColWidth
Col5 = Left + 4*ColWidth
Col6 = Left + 5*ColWidth
NColForBox = 6
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (800,600))  
      self.panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      self.DataFolder = "../../data"
      self.VisitFolderPath = 'empty'
      # Setup the Participant ID entry
      self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Participant ID:", pos = (Col1,Row1))
      self.PartID = wx.TextCtrl(self.panel,-1,'9999999',size=(ButtonWidth,-1),pos = (Col2,Row1))
      self.btnPartEntry = wx.Button(self.panel,-1,label = "Enter", pos = (Col3,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btnPartEntry.Bind(wx.EVT_BUTTON, self.OnCickPartEntry)
      # Create Default values for the load levels for the two tasks
      self.FRTBlockLoadLevels = '0.0 0.125 0.25 0.375 0.5'
      self.DMSBlockLoadLevels = '1 3 5 6 7'
      self.VSTMBlockLoadLevels = '1 2 3 4 5'     
      
      # #### Row 
      # STROOP
      CurrentRow = Row2
      self.title1 = wx.StaticText(self.panel, -1, label = "Stroop", pos = (Col1+LabelOffset/2,CurrentRow+LabelOffset))
      # Buttons
      self.btnR1C2 = wx.Button(self.panel,-1,"Color", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C2.Bind(wx.EVT_BUTTON,self.OnClickedR1C2) 
      self.btnR1C3 = wx.Button(self.panel,-1,"Word", pos = (Col3,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C3.Bind(wx.EVT_BUTTON,self.OnClickedR1C3) 
      self.btnR1C4 = wx.Button(self.panel,-1,"ColorWord", pos = (Col4,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C4.Bind(wx.EVT_BUTTON,self.OnClickedR1C4)
      
      
      # Box
      Row1Box = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (Col1,CurrentRow-5))
      # Checkboxes
      self.cbR1C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
      self.cbR1C3 = wx.CheckBox(self.panel, -1, label = "", pos = (Col3 + ButtonWidth+5,CurrentRow))
      self.cbR1C4 = wx.CheckBox(self.panel, -1, label = "", pos = (Col4 + ButtonWidth+5,CurrentRow))
      
      # #### Row 
      CurrentRow = Row3
      self.titleR2 = wx.StaticText(self.panel, -1, label = "Card Sort", pos = (Col1+LabelOffset/2,CurrentRow+LabelOffset))
      # Buttons
      self.btnR2C2 = wx.Button(self.panel,-1,"WCST", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR2C2.Bind(wx.EVT_BUTTON,self.OnClickedR2C2) 
#      self.btnR2C3 = wx.Button(panel,-1,"Demo", pos = (Col3,Row2), size = ((ButtonWidth, ButtonHeight))) 
#      self.btnR2C3.Bind(wx.EVT_BUTTON,self.OnClickedR2C3) 
#      self.btnR2C4 = wx.Button(panel,-1,"Demo", pos = (Col4,Row2), size = ((ButtonWidth, ButtonHeight))) 
#      self.btnR2C4.Bind(wx.EVT_BUTTON,self.OnClickedR2C4) 
      # Box
      Row1BoxR2 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (Col1,CurrentRow-5))
      # Checkboxes
      self.cbR2C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
#      self.cbR2C3 = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row2))
#      self.cbR2C4 = wx.CheckBox(panel, -1, label = "", pos = (Col4 + ButtonWidth+5,Row2))
# ###################
      CurrentRow = Row4
#      # #### Row 3
      self.titleR3 = wx.StaticText(self.panel, -1, label = "Spatial/Dots", pos = (Col1+LabelOffset/2,CurrentRow+LabelOffset))
#      # Buttons
      self.btnR3C2 = wx.Button(self.panel,-1,"Demo", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C2.Bind(wx.EVT_BUTTON,self.OnClickedR3C2) 
      self.btnR3C3 = wx.Button(self.panel,-1,"Stair", pos = (Col3,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C3.Bind(wx.EVT_BUTTON,self.OnClickedR3C3) 
      self.btnR3C4 = wx.Button(self.panel,-1,"Block", pos = (Col4,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C4.Bind(wx.EVT_BUTTON,self.OnClickedR3C4) 
#      # Box
      Row1BoxR3 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (Col1,CurrentRow-5))
      # Checkboxes
      self.cbR3C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
      self.cbR3C3 = wx.CheckBox(self.panel, -1, label = "", pos = (Col3 + ButtonWidth+5,CurrentRow))
      self.cbR3C4 = wx.CheckBox(self.panel, -1, label = "", pos = (Col4 + ButtonWidth+5,CurrentRow))
# ###################
      CurrentRow = Row5
#      # #### Row 3
      self.titleR5 = wx.StaticText(self.panel, -1, label = "DMS/Letters", pos = (Col1+LabelOffset/2,CurrentRow+LabelOffset))
#      # Buttons
      self.btnR5C2 = wx.Button(self.panel,-1,"Demo", pos = (Col2,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C2.Bind(wx.EVT_BUTTON,self.OnClickedR5C2) 
      self.btnR5C3 = wx.Button(self.panel,-1,"Stair", pos = (Col3,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C3.Bind(wx.EVT_BUTTON,self.OnClickedR5C3) 
      # Text box for the capacity value
      self.txtR5C4 = wx.StaticText(self.panel, -1, label = "Cap =", pos = (Col4+10,CurrentRow+LabelOffset))
      self.txtR5C5 = wx.StaticText(self.panel, -1, label = "0000000", pos = (Col5-ColWidth/2+5,CurrentRow+LabelOffset))  
      self.btnR5C5 = wx.Button(self.panel,-1,"Load", pos = (Col5+20,CurrentRow), size = ((ButtonWidth/2+5, ButtonHeight))) 
      Row5BoxR5 = wx.StaticBox(self.panel, -1, size = ((ColWidth*2),RowWidth-5), pos = (Col4,CurrentRow-5))
      
      self.btnR5C6 = wx.Button(self.panel,-1,"Block", pos = (Col6,CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR5C6.Bind(wx.EVT_BUTTON,self.OnClickedR5C6) 
#      # Box
      Row1BoxR5 = wx.StaticBox(self.panel, -1, size = ((ColWidth+5)*NColForBox,RowWidth-5), pos = (Col1,CurrentRow-5))
      # Checkboxes
      self.cbR5C2 = wx.CheckBox(self.panel, -1, label = "", pos = (Col2 + ButtonWidth+5,CurrentRow))
      self.cbR5C3 = wx.CheckBox(self.panel, -1, label = "", pos = (Col3 + ButtonWidth+5,CurrentRow))
      self.cbR5C6 = wx.CheckBox(self.panel, -1, label = "", pos = (Col6 + ButtonWidth+5,CurrentRow))

# ##########
      self.btnClose = wx.Button(self.panel,-1,"Close", pos = (Col1,Row8), size = ((ButtonWidth, ButtonHeight))) 
      self.btnClose.Bind(wx.EVT_BUTTON,self.CloseGUI) 
      
      self.Centre() 
      self.Show() 
      self.Fit()  
      
  
   def DisableAll(self): 
      for child in self.panel.GetChildren():
        # Diable all buttons except the button to enter the participant ID
        if isinstance(child, wx.Button):
            if child.Label != "Enter":
                child.Disable()
   
   def EnableAll(self): 
      for child in self.panel.GetChildren():
        # Diable all buttons except the button to enter the participant ID
        if isinstance(child, wx.Button):
            if child.Label != "Enter":
                child.Enable()
                
   def LoadVSTMCapacity(self, event):
      pass
   
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
                    print 'You selected: %s\n' % dlg.GetStringSelection()
                    self.VisitFolderName = dlg.GetStringSelection()
                    self.VisitFolderPath = os.path.join(self.PartFolder, self.VisitFolderName)
                dlg.Destroy()
            else:
                # Make a new visit
                # New visit folders will increment the visit number V002, V003, etc
                self.VisitFolderName = '%s_V00%d'%(data.getDateStr(),ListOfVisitFolders[-1]+1)
                self.VisitFolderPath = os.path.join(self.PartFolder,self.VisitFolderName)
                os.mkdir(self.VisitFolderPath)
        print(self.VisitFolderPath)
        
        # Add the path name to the GUI
        self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Output folder: %s"%(self.VisitFolderName), pos = (Col4,Row1))
        
      
   def OnCickPartEntry(self, event):
      btnName = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnName))
      # Check to see if there is a participant folder for this person
      self.CheckPartFolder()
      self.CheckVisitFolder()
      # Enabale the buttons again
      self.EnableAll()
    # Row 1 Functions      
   
   def CreatePartFolder(self):
      os.mkdir(self.PartFolder)
      
   def OnClickedR1C2(self, event): 
      btnR1C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C2Label))
      core.shellCall([sys.executable, "../Stroop/StroopColor_lastrun.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR1C2.SetValue(True)
      
   def OnClickedR1C3(self, event): 
      btnR1C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C3Label))
      core.shellCall([sys.executable, "../Stroop/StroopWord_lastrun.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR1C3.SetValue(True)
      
   def OnClickedR1C4(self, event): 
      btnR1C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C4Label))
      core.shellCall([sys.executable, "../Stroop/StroopColorWord_lastrun.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR1C4.SetValue(True)      

   # Row 2 Functions   
   def OnClickedR2C2(self, event): 
      btnR2C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR2C2Label))
      core.shellCall([sys.executable, "../WCST/WCST_v2.py", self.PartID.GetValue(), self.VisitFolderPath])#, self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR2C2.SetValue(True)
      
   def OnClickedR2C3(self, event): 
      btnR2C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR2C3Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR2C3.SetValue(True)
      
   def OnClickedR2C4(self, event): 
      btnR2C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR2C4Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR2C4.SetValue(True)      
   
   # Row 3 Functions   
   def OnClickedR3C2(self, event): 
      btnR3C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C2Label))
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTM_CirclesInGrid_DEMOv1.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR3C2.SetValue(True)
      
   def OnClickedR3C3(self, event): 
      btnR3C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C3Label))
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTM_CirclesInGridStaircase_v2.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR3C3.SetValue(True)
      
   def OnClickedR3C4(self, event): 
      btnR3C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C4Label))
      VSTMCapacity = 7
      self.VSTMBlockLoadLevels = self.CreateVSTMList5(VSTMCapacity)
      print('With a capacity of %0.1f, the load levels will be:'%(VSTMCapacity))
      print( self.VSTMBlockLoadLevels)
      core.shellCall([sys.executable, "../VSTMPsychopyFiles/VSTM_CirclesInGrid_v4.py", self.PartID.GetValue(), self.VisitFolderPath, self.VSTMBlockLoadLevels])  
      self.cbR3C4.SetValue(True)  

   # Row 5 Functions   
   def OnClickedR5C2(self, event): 
      btnR5C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C2Label))
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMSDemo_GUI.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR5C2.SetValue(True)
      
   def OnClickedR5C3(self, event): 
      btnR5C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C3Label))
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMSStairCase_v3.py", self.PartID.GetValue(), self.VisitFolderPath])
      self.cbR5C3.SetValue(True)
      
   def OnClickedR5C6(self, event): 
      btnR5C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR5C4Label))
      core.shellCall([sys.executable, "../DMSPsychopyFiles/DMS_Adaptive5Load_v3.py", self.PartID.GetValue(), self.VisitFolderPath, self.DMSBlockLoadLevels])  
      self.cbR5C4.SetValue(True)  
   
   def CloseGUI(self,event):
        self.Close()
      
app = wx.App() 
# Create the GUI
MyGui = Mywin(None,  'NCM Lab') 
# Disable all the buttons except teh Part ID entry 
MyGui.DisableAll()
app.MainLoop()
