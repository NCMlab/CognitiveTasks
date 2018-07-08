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
      self.PartID = wx.TextCtrl(panel,-1,'9999999',size=(100,30),pos = (140,48))
      self.PartIDLabel = wx.StaticText(panel, -1, label = "Counterbalance", pos = (250,55))
      self.CounterBalCB = wx.CheckBox(panel, -1, label = "", pos = (350,55))
      
        
      font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
    # Create a box for the Face task buttons 
      FacesBox = wx.StaticBox(panel, -1, size = (350,140), pos = (30,80))
      # create a label for the faces box
      self.title2 = wx.StaticText(panel, -1, label = "VisualSTM", pos = (50,90))
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
#      # Button FRT DEMO
#      self.btn = wx.Button(panel,-1,"Demo", pos = (45,110)) 
#      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
#      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTDemo) 
#      # Checkbox for FRT DEMO
#      self.FRTDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,115))

#      # Button VSTM DEMO
      self.btn = wx.Button(panel,-1,"Demo", pos = (45,110)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedVSTMDemo) 
      # Checkbox for FRT DEMO
      self.VSTMDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,115))

      # Button VSTM STAIRCASE
      self.btn = wx.Button(panel,-1,"Staircase", pos = (45,130)) 
      self.VSTMStairCaseCapText = wx.StaticText(panel, -1, label = "Capacity = ", pos = (170,135))
      self.VSTMStairCaseCapText = wx.StaticText(panel, -1, label = "0000000", pos = (250,135))      
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedVSTMStair) 
    # Checkbox for VSTM staircase
      self.VSTMStairCB = wx.CheckBox(panel, -1, label = "", pos = (140,135))

      # Manual entry button for VSTM Capacity
      self.btn = wx.Button(panel,-1,"Enter", pos = (317,132),size = (45,13)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedVSTMCapEnter) 
      # self.btn = wx.Button(panel,-1,"Load", pos = (317,150),size = (45,13)) 

      # Button VSTM Run 1
      self.btn = wx.Button(panel,-1,"VSTM Run 1", pos = (45,150)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedVSTMBlock) 
    # Checkbox for VSTM staircase
      self.VSTMBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,155))

      # Button VSTM Run 2
      self.btn = wx.Button(panel,-1,"VSTM Run 2", pos = (45,170)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedVSTMBlock) 
    # Checkbox for VSTM staircase
      self.VSTMBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,175))

#      # Button FRT BLOCK ONE
#      self.btn = wx.Button(panel,-1,"FRT Run 1", pos = (45,150)) 
#      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
#      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTBlock)       
#      # Checkbox for FRT BLOCK ONE
#      self.FRTBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,155))
#      # =========================================================================
#      # Button FRT BLOCK TWO
#      self.btn = wx.Button(panel,-1,"FRT Run 2", pos = (45,170)) 
#      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
#      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedFRTBlock)       
#      # Checkbox for FRT BLOCK TWO
#      self.FRTBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,175))


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
      self.btn = wx.Button(panel,-1,"DMS Run 1", pos = (45,280)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSBlock) 
    # Checkbox for DMS BLOCK ONE
      self.DMSBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,285))

    # Button DMS BLOCK TWO
      self.btn = wx.Button(panel,-1,"DMS Run 2", pos = (45,300)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSBlock) 
    # Checkbox for DMS BLOCK TWO
      self.DMSBlockCB2 = wx.CheckBox(panel, -1, label = "", pos = (140,305))

## Words BUTTONS
      # Button WORD DEMO
      self.btn = wx.Button(panel,-1,"Demo", pos = (45,375)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON, self.OnClickedWORDDemo) 
      
      # Checkbox for WORD Demo
      # self.WORDDEMOCB = wx.CheckBox(panel, -1, label = "", pos = (140,380))


      # Button WORD STAIRCASE
      #self.btn = wx.Button(panel,-1,"Staircase", pos = (45,395)) 
      #vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      # self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSStair) 
      #self.WORDStairCaseCapText = wx.StaticText(panel, -1, label = "Capacity = ", pos = (170,395))
      #self.WORDStairCaseCapText = wx.StaticText(panel, -1, label = "0000000", pos = (250,395))
      
      # Checkbox for WORD staircase
      # self.WORDStairCB = wx.CheckBox(panel, -1, label = "", pos = (140,400))
      
      # Manual entry button for WORD Capacity
      #self.btn = wx.Button(panel,-1,"Enter", pos = (317,400),size = (45,13)) 
      #self.btn = wx.Button(panel,-1,"Enter", pos = (317,132),size = (45,13)) 
      #vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      #self.btn.Bind(wx.EVT_BUTTON,self.OnClickedDMSCapEnter) 

      # Button WORD BLOCK ONE
      self.btn = wx.Button(panel,-1,"SR Run 1", pos = (45,415)) 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClickedWORDEV) 
    # Checkbox for WORD BLOCK ONE
      self.WORDBlockCB1 = wx.CheckBox(panel, -1, label = "", pos = (140,420))

    # Button WORD BLOCK TWO
      self.btn = wx.Button(panel,-1,"SR Run 2", pos = (45,435)) 
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
      self.VSTMBlockLoadLevels = '1 2 3 4 5'     
      self.Centre() 
      self.Show() 
      self.Fit()  
 		
   # Here I have passed a paramater to the call of the task.
   # In the program you would add the following to use the input arguments
   # dlg = gui.DlgFromDict(dictionary=expInfo, title=sys.argv[1])
   
   # Run the Faces demo
   def OnClickedFRTDemo(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btn))
      core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.FRTDEMOCB.SetValue(True)
    
   def OnClickedVSTMDemo(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btn))
      core.shellCall([sys.executable, "VSTMPsychopyFiles/VSTM_CirclesInGrid_DEMOv1.py", self.PartID.GetValue()])
      self.VSTMDEMOCB.SetValue(True)
      
    # run the faces staircase
   def OnClickedVSTMStair(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btn))
      self.VSTMStairCaseDateStr = data.getDateStr()
      core.shellCall([sys.executable, "VSTMPsychopyFiles/VSTM_CirclesInGridStaircase_v2.py", self.PartID.GetValue()])
      # after the task is run read the capicity file
      self.LoadVSTMCapacity(self)
      
   def LoadVSTMCapacity(self, event):
        self.VSTMStairCB.SetValue(True)
        task = 'VSTMstair'
        dateStr = self.VSTMStairCaseDateStr
        #dateStr = "2017_Jul_27_1536"
        PartID = self.PartID.GetValue()
        #fileName = task + PartID + "_"+ dateStr
        OutDir = '..' + os.sep + 'data' + os.sep + PartID + os.sep
        CapFile=open(OutDir + 'CAPACITY_%s_%s_%s.txt' % (task, PartID, dateStr),'r')
        
        #CapFile = open(os.path.join("data","CAPACITY_" + fileName + ".txt"),'r')
        # Read the capcity from the file and make it a local variable
        self.VSTMStairCaseCap = CapFile.read()
        # Set the GUI label for capacity
        self.VSTMStairCaseCapText.SetLabel(self.VSTMStairCaseCap)
        # close the file
        CapFile.close()
        # remove the file
        # os.Remove(os.path.join("data","CAPACITY_" + fileName + ".txt"))
        # Once the capacity is loaded, calculate the load levels
        self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMStairCaseCap)
        
        
   def OnClickedWORDDemo(self, event):
       print(self.CounterBalCB.GetValue())
       btn = event.GetEventObject().GetLabel() 
       CounterBalFlag = str(self.CounterBalCB.GetValue())
       print("Label of pressed button = %s"%(btn ))
       Tag = 'WordDemo'
       print self.PartID.GetValue()
       # print self.DMSBlockLoadLevels
       #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
       core.shellCall([sys.executable, "SemanticRichness/BlockBased/SemanticRichnessBlockBasedDEMOv2.py", self.PartID.GetValue(),CounterBalFlag,Tag])
       #self.WORDBlockCB1.SetValue(True)
       
    
   def OnClickedFRTBlock(self, event): 
        btn = event.GetEventObject().GetLabel() 
        print("Label of pressed button = "%(btn ))
        print self.PartID.GetValue()
        print self.FRTBlockLoadLevels
        core.shellCall([sys.executable, "FRTPsychopyFiles/FRT_Adaptive.py", self.PartID.GetValue(), self.FRTBlockLoadLevels])
        self.FRTBlockCB1.SetValue(True)

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
      FontSize = '60'
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btn ))
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMSDemo_GUI.py", self.PartID.GetValue(),FontSize])
      self.DMSDEMOCB.SetValue(True)

   def OnClickedDMSStair(self, event): 
      FontSize = '60'
      self.DMSStairCaseDateStr = data.getDateStr()
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btn ))
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMSStairCase_v2.py", self.PartID.GetValue(),FontSize])
      self.LoadDMSCapacity(self)
      
   def OnClickedDMSBlock(self, event): 
      FontSize = '60'
      btn = event.GetEventObject().GetLabel() 
      CounterBalFlag = str(self.CounterBalCB.GetValue())
      print("Label of pressed button = %s"%(btn ))
      
      if btn == 'DMS Run 1':
        Tag = '1'
      elif btn == 'DMS Run 2':
        Tag = '2'
      else:
        Tag = '9'
      print self.PartID.GetValue()
      print self.DMSBlockLoadLevels
      #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive5Load_v3.py", self.PartID.GetValue(), self.DMSBlockLoadLevels, CounterBalFlag, Tag, FontSize])
      if Tag == '1':
        self.DMSBlockCB1.SetValue(True)
      else:  
        self.DMSBlockCB2.SetValue(True)
   
   def OnClickedVSTMBlock(self, event): 
      btn = event.GetEventObject().GetLabel() 
      CounterBalFlag = str(self.CounterBalCB.GetValue())
      print("Label of pressed button = %s"%(btn ))
      
      if btn == 'VSTM Run 1':
        Tag = '1'
      elif btn == 'VSTM Run 2':
        Tag = '2'
      else:
        Tag = '9'
      print self.PartID.GetValue()
      print self.VSTMBlockLoadLevels
      #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      core.shellCall([sys.executable, "VSTMPsychopyFiles/VSTM_CirclesInGrid_v4.py", self.PartID.GetValue(), self.VSTMBlockLoadLevels, CounterBalFlag, Tag])
      if Tag == '1':
        self.VSTMBlockCB1.SetValue(True)
      else:  
        self.VSTMBlockCB2.SetValue(True)   
   
   
   def OnClickedWORDEV(self, event): 
      btn = event.GetEventObject().GetLabel() 
      CounterBalFlag = str(self.CounterBalCB.GetValue())
      print("Label of pressed button = %s"%(btn ))
      if btn == 'SR Run 1':
        Tag = '1'
      elif btn == 'SR Run 2':
        Tag = '2'
      else:
        Tag = '9'
      print self.PartID.GetValue()
      # print self.DMSBlockLoadLevels
      #core.shellCall([sys.executable, "DMSPsychopyFiles/DMS_Adaptive_v2.py", self.PartID.GetValue(), self.DMSBlockLoadLevels])
      core.shellCall([sys.executable, "SemanticRichness/BlockBased/SemanticRichnessBlockBasedv2.py", self.PartID.GetValue(),CounterBalFlag,Tag])
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
                print("Out of Range")
        else:
            print("user cancelled")
        return str(Capacity)
        
   def OnClickedVSTMCapEnter(self,event):
        self.VSTMStairCaseCap = self.ManualEntryCapacity([0.0, 36])
        self.VSTMStairCaseCapText.SetLabel(self.VSTMStairCaseCap)
        self.VSTMBlockLoadLevels = self.CreateVSTMList5(self.VSTMStairCaseCap)

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