#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Wed Jul 26 20:20:27 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008

XX Make GUI copy of Demos
XX Allow Both Demo to take subid as input
XX Add additional checkboxes
XX Fix block based
-Results data for Faces Block goes back to the faces /data folder
-The DMS task calls a single letter list up, I need to recreate this list so that 9 letters are included. 
-I think I will have each block dynamically make a selection of trials. So if the list of all trials has 10 
trials per load then this should be straightforward.
-Change the selection method to random so that a random ordering from the list is used for the block.
I can create a dictionary of the rows to select for each load level, or be more dynamic.
Add functionality to the checkboxes
Add button to "lock-in" a subject ID to prevent it from being accidentally changed"


"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os  # handy system and path functions
import sys  # to get file system encoding
import wx
import numpy as np
# Ensure that relative paths start from the same directory as this script

_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# https://www.tutorialspoint.com/wxpython/wxpython_buttons.htm
# https://groups.google.com/forum/#!topic/psychopy-users/3V8YUAwsdIs

class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (400,600))  
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      # Static Text
     ## TitleFont = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.ALIGN_CENTER) 
      TitleBox = wx.StaticBox(panel, -1, size = (380,50), pos = (10, 0))
      # Create the title
      self.title1 = wx.StaticText(panel, -1, label = "Neural Cognitive Mapping", pos = (30,15))
     ## self.title1.SetFont(TitleFont)
      # Create a box around the title
      TiltleBox2 = wx.StaticBox(panel, -1, size = (360,40), pos = (20, 45))
      # Create an input for the Participant ID
      self.PartIDLabel = wx.StaticText(panel, -1, label = "Participant ID:", pos = (40,55))
      self.PartID = wx.TextCtrl(panel,-1,'9999999',size=(100,30),pos = (200,48))

      font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
    # Create a box for the Face task buttons 
      FacesBox = wx.StaticBox(panel, -1, size = (350,140), pos = (30,80))
      # create a label for the faces box
      self.title2 = wx.StaticText(panel, -1, label = "Face Tasks", pos = (50,90))
      self.title2.SetFont(font) 
      
      # Create a box for the letters buttons 
      LettersBox = wx.StaticBox(panel, -1, size = (350,120), pos = (30,215))
      # Create a label for the letters box
      self.title3 = wx.StaticText(panel, -1, label = "Letter Tasks", pos = (50,220))
      # Create a box for the WORDS buttons 
      WordsBox = wx.StaticBox(panel, -1, size = (350,120), pos = (30,350))
      self.title3.SetFont(font) 
      
      # Create a label for the WORDS box
      self.title4 = wx.StaticText(panel, -1, label = "Word Tasks", pos = (50,355))
      self.title4.SetFont(font) 

## FACES BUTTONS
      # Button FRT DEMO
      self.btn = wx.Button(panel,-1,"Demo", pos = (45,110)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTDemo) 
      # Checkbox for FRT DEMO
      self.FRTDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,115))

      # Button FRT STAIRCASE
      self.btn = wx.Button(panel,-1,"Staircase", pos = (45,130)) 
      self.FRTStairCaseCapText = wx.StaticText(panel, -1, label = "Capacity = ", pos = (170,135))
      self.FRTStairCaseCapText = wx.StaticText(panel, -1, label = "0000000", pos = (250,135))      
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTStair) 
    # Checkbox for FRT staircase
      self.FRTStairCB = wx.CheckBox(panel, -1, label = "", pos = (140,135))
      
      # Manual entry button for FRT Capacity
      self.btn = wx.Button(panel,-1,"Enter", pos = (317,132),size = (45,13)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTCapEnter) 
      # self.btn = wx.Button(panel,-1,"Load", pos = (317,150),size = (45,13)) 
      
      # Button FRT BLOCK ONE
      self.btn = wx.Button(panel,-1,"Block One", pos = (45,150)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTBlock)       
      # Checkbox for FRT BLOCK ONE
      self.FRTBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,155))
      # =========================================================================
      # Button FRT BLOCK TWO
      self.btn = wx.Button(panel,-1,"Block Two", pos = (45,170)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTBlock)       
      # Checkbox for FRT BLOCK TWO
      self.FRTBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,175))


## LETTERS BUTTONS
      # Button DMS DEMO
      self.btn = wx.Button(panel,-1,"Demo", pos = (45,240)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSDemo) 
      
      # Checkbox for DMS Demo
      self.DMSDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,245))


      # Button DMS STAIRCASE
      self.btn = wx.Button(panel,-1,"Staircase", pos = (45,260)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSStair) 
      self.DMSStairCaseCapText = wx.StaticText(panel, -1, label = "Capacity = ", pos = (170,260))
      self.DMSStairCaseCapText = wx.StaticText(panel, -1, label = "0000000", pos = (250,260))
      
      # Checkbox for DMS staircase
      self.DMSStairCB = wx.CheckBox(panel, -1, label = "", pos = (140,265))
      # Manual entry button for DMS Capacity
      self.btn = wx.Button(panel,-1,"Enter", pos = (317,260),size = (45,13)) 
      #self.btn = wx.Button(panel,-1,"Enter", pos = (317,132),size = (45,13)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSCapEnter) 

      # Button DMS BLOCK ONE
      self.btn = wx.Button(panel,-1,"Block One", pos = (45,280)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSBlock) 
    # Checkbox for DMS BLOCK ONE
      self.DMSBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,285))

    # Button DMS BLOCK TWO
      self.btn = wx.Button(panel,-1,"Block Two", pos = (45,300)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSBlock) 
    # Checkbox for DMS BLOCK TWO
      self.DMSBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,305))

## Words BUTTONS
      # Button WORD DEMO
      self.btn = wx.Button(panel,-1,"Demo", pos = (45,375)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSDemo) 
      
      # Checkbox for WORD Demo
      self.WORDDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,380))


      # Button WORD STAIRCASE
      self.btn = wx.Button(panel,-1,"Staircase", pos = (45,395)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      # self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSStair) 
      self.WORDStairCaseCapText = wx.StaticText(panel, -1, label = "Capacity = ", pos = (170,395))
      self.WORDStairCaseCapText = wx.StaticText(panel, -1, label = "0000000", pos = (250,395))
      
      # Checkbox for WORD staircase
      self.WORDStairCB = wx.CheckBox(panel, -1, label = "", pos = (140,400))
      
      # Manual entry button for WORD Capacity
      self.btn = wx.Button(panel,-1,"Enter", pos = (317,400),size = (45,13)) 
      #self.btn = wx.Button(panel,-1,"Enter", pos = (317,132),size = (45,13)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSCapEnter) 

      # Button WORD BLOCK ONE
      self.btn = wx.Button(panel,-1,"EV Run One", pos = (45,415)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedWORDEV) 
    # Checkbox for WORD BLOCK ONE
      self.WORDBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,420))

    # Button WORD BLOCK TWO
      self.btn = wx.Button(panel,-1,"EV Run Two", pos = (45,435)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedWORDEV) 
    # Checkbox for WORD BLOCK TWO
      self.WORDBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,440))

# Create a Close button to close the GUI
      self.btn = wx.Button(panel,-1,"Close", pos = (140,480)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.CloseGUI) 

    # Create Default values for the load levels for the two tasks
      self.FRTBlockLoadLevels = '0.0 0.125 0.25 0.375 0.5'
      self.DMSBlockLoadLevels = '1 3 5 6 7'
           
      self.Centre() 
      self.Show() 
      self.Fit()  
 		
   # Here I have passed a paramater to the call of the task.
   # In the program you would add the following to use the input arguments
   # dlg = gui.DlgFromDict(dictionary=expInfo, title=sys.argv[1])
   
   # Run the Faces demo
   def OnClickedFRTDemo(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.FRTDEMOCB.SetValue(True)
      
    # run the faces staircase
   def OnClickedFRTStair(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      self.FRTStairCaseDateStr = data.getDateStr()
      core.shellCall([sys.executable, "FRTPsychopyFiles/FRTStairCase_v1.py", self.PartID.GetValue()])
      # after the task is run read the capicity file
      self.LoadFRTCapacity(self)
      
   def LoadFRTCapacity(self, event):
        self.FRTStairCB.SetValue(True)
        task = 'FRTstair_'
        dateStr = self.FRTStairCaseDateStr
        #dateStr = "2017_Jul_27_1536"
        PartID = self.PartID.GetValue()
        #fileName = task + PartID + "_"+ dateStr
        OutDir = '..' + os.sep + 'data' + os.sep + PartID + os.sep
        CapFile=open(OutDir + 'CAPACITY_%s%s_%s.txt' % (task, PartID, dateStr),'r')
        
        #CapFile = open(os.path.join("data","CAPACITY_" + fileName + ".txt"),'r')
        # Read the capcity from the file and make it a local variable
        self.FRTStairCaseCap = CapFile.read()
        # Set the GUI label for capacity
        self.FRTStairCaseCapText.SetLabel(self.FRTStairCaseCap)
        # close the file
        CapFile.close()
        # remove the file
        # os.Remove(os.path.join("data","CAPACITY_" + fileName + ".txt"))
        # Once the capacity is loaded, calculate the load levels
        self.FRTBlockLoadLevels = self.CreateFRTList(self.FRTStairCaseCap)
        
   def OnClickedFRTBlock(self, event): 
        btn = event.GetEventObject().GetLabel() 
        print "Label of pressed button = ",btn 
        print self.PartID.GetValue()
        print self.FRTBlockLoadLevels
        core.shellCall([sys.executable, "FRTPsychopyFiles/FRT_Adaptive.py", self.PartID.GetValue(), self.FRTBlockLoadLevels])
        self.FRTBlockCB.SetValue(True)

   def LoadDMSCapacity(self, event):
        self.DMSStairCB.SetValue(True)
        task = 'DMSstair_'
        dateStr = self.DMSStairCaseDateStr
        #dateStr = "2017_Jul_27_1536"
        PartID = self.PartID.GetValue()
        #fileName = task + PartID + "_"+ dateStr
        OutDir = '..' + os.sep + 'data' + os.sep + PartID + os.sep
        CapFile=open(OutDir + 'CAPACITY_%s%s_%s.txt' % (task, PartID, dateStr),'r')
        self.DMSStairCaseCap = CapFile.read()
        self.DMSStairCaseCapText.SetLabel(self.DMSStairCaseCap)
        CapFile.close()
        #os.Remove(os.path.join("data","CAPACITY_" + fileName + ".txt"))
        self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSStairCaseCap)
      
   def OnClickedDMSDemo(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMSDemo_GUI.py", self.PartID.GetValue()])
      self.DMSDEMOCB.SetValue(True)

   def OnClickedDMSStair(self, event): 
      self.DMSStairCaseDateStr = data.getDateStr()
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMSStairCase_v2.py", self.PartID.GetValue()])
      self.LoadDMSCapacity(self)
      
   def OnClickedDMSBlock(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      print self.PartID.GetValue()
      print self.DMSBlockLoadLevels
      #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive5Load_v3.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      self.DMSBlockCB.SetValue(True)
   
   def OnClickedWORDEV(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print "Label of pressed button = ",btn 
      if btn == 'EV Run One':
        Tag = '1'
      elif btn == 'EV Run Two':
        Tag = '2'
      else:
        Tag = '9'
      print self.PartID.GetValue()
      # print self.DMSBlockLoadLevels
      #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      core.shellCall([sys.executable, "SemanticRichness/LexicalDecisionEVRun.py", self.PartID.GetValue(),Tag])
      #self.WORDBlockCB1.SetValue(True)

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

   def CreateFRTList(self, FRTCapacity):
        # Made a small change here so that the capacity will be load level 5.
        Limit = np.float(FRTCapacity)*1.25
        #FRTList = range(0,6,1)Limit,Limit/(6-1))
        FRTList = np.array(range(0,6,1))/(6.0-1)*Limit
        # Convert this array to a string so it can be passed as an argument
        FRTList = ' '.join(str(e) for e in FRTList)
        return FRTList
                
   def ManualEntryCapacity(self,Range):
        myDlg = gui.Dlg(title=u"NCM Lab", labelButtonOK=' OK ', labelButtonCancel=' Cancel ',)
        myDlg.addField(u'Capacity:')
        myDlg.show()  # show dialog and wait for OK or Cancel
        Capacity = -9999
        if myDlg.OK:  # then the user pressed OK
            thisInfo = myDlg.data
    
            if (float(thisInfo[0]) >= float(Range[0])) and (float(thisInfo[0]) <= float(Range[1])):
                print "Capacity = " + str(thisInfo)
                Capacity = float(thisInfo[0])
            else:
                print "Out of Range"
        else:
            print 'user cancelled'
        return str(Capacity)
        
   def OnClickedFRTCapEnter(self,event):
        self.FRTStairCaseCap = self.ManualEntryCapacity([0.0, 1.0])
        self.FRTStairCaseCapText.SetLabel(self.FRTStairCaseCap)
        self.FRTBlockLoadLevels = self.CreateFRTList(self.FRTStairCaseCap)

   def OnClickedDMSCapEnter(self,event):
        self.DMSStairCaseCap = self.ManualEntryCapacity([0.0, 9.0])
        self.DMSStairCaseCapText.SetLabel(self.DMSStairCaseCap)
        self.DMSBlockLoadLevels = self.CreateDMSList5(self.DMSStairCaseCap)

   def CloseGUI(self,event):
        self.Close()
        
             
app = wx.App() 
Mywin(None,  'NCM Lab') 
app.MainLoop()


#import sys
#from psychopy import core
#core.shellCall([sys.executable, "20150418_memo_1a.py"])
#core.shellCall([sys.executable, "20150418_memo_1b.py"])
#core.shellCall([sys.executable, "20150418_memo_1c.py"])