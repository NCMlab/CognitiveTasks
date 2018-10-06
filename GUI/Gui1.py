from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
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

Col1 = Left
Col2 = Left + ColWidth
Col3 = Left + 2*ColWidth
Col4 = Left + 3*ColWidth
Col5 = Left + 4*ColWidth
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (600,600))  
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      
      # #### Row 1
      self.title1 = wx.StaticText(panel, -1, label = "VisualSTM", pos = (Col1+LabelOffset/2,Row1+LabelOffset))
      # Buttons
      self.btnR1C2 = wx.Button(panel,-1,"Demo", pos = (Col2,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C2.Bind(wx.EVT_BUTTON,self.OnClickedR1C2) 
      self.btnR1C3 = wx.Button(panel,-1,"Demo", pos = (Col3,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C3.Bind(wx.EVT_BUTTON,self.OnClickedR1C3) 
      self.btnR1C4 = wx.Button(panel,-1,"Demo", pos = (Col4,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR1C4.Bind(wx.EVT_BUTTON,self.OnClickedR1C4) 
      
      # Box
      Row1Box = wx.StaticBox(panel, -1, size = ((ColWidth+5)*5,RowWidth-5), pos = (Col1,Row1-5))
      # Checkboxes
      self.cbR1C2 = wx.CheckBox(panel, -1, label = "", pos = (Col2 + ButtonWidth+5,Row1))
      self.cbR1C3 = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row1))
      self.cbR1C4 = wx.CheckBox(panel, -1, label = "", pos = (Col4 + ButtonWidth+5,Row1))
      
      # #### Row 2
      self.titleR2 = wx.StaticText(panel, -1, label = "VisualSTM", pos = (Col1+LabelOffset/2,Row2+LabelOffset))
      # Buttons
      self.btnR2C2 = wx.Button(panel,-1,"Demo", pos = (Col2,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR2C2.Bind(wx.EVT_BUTTON,self.OnClickedR2C2) 
      self.btnR2C3 = wx.Button(panel,-1,"Demo", pos = (Col3,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR2C3.Bind(wx.EVT_BUTTON,self.OnClickedR2C3) 
      self.btnR2C4 = wx.Button(panel,-1,"Demo", pos = (Col4,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR2C4.Bind(wx.EVT_BUTTON,self.OnClickedR2C4) 
      # Box
      Row1BoxR2 = wx.StaticBox(panel, -1, size = ((ColWidth+5)*5,RowWidth-5), pos = (Col1,Row2-5))
      # Checkboxes
      self.cbR2C2 = wx.CheckBox(panel, -1, label = "", pos = (Col2 + ButtonWidth+5,Row2))
      self.cbR2C3 = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row2))
      self.cbR2C4 = wx.CheckBox(panel, -1, label = "", pos = (Col4 + ButtonWidth+5,Row2))

      # #### Row 3
      self.titleR3 = wx.StaticText(panel, -1, label = "VisualSTM", pos = (Col1+LabelOffset/2,Row3+LabelOffset))
      # Buttons
      self.btnR3C2 = wx.Button(panel,-1,"Demo", pos = (Col2,Row3), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C2.Bind(wx.EVT_BUTTON,self.OnClickedR3C2) 
      self.btnR3C3 = wx.Button(panel,-1,"Demo", pos = (Col3,Row3), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C3.Bind(wx.EVT_BUTTON,self.OnClickedR3C3) 
      self.btnR3C4 = wx.Button(panel,-1,"Demo", pos = (Col4,Row3), size = ((ButtonWidth, ButtonHeight))) 
      self.btnR3C4.Bind(wx.EVT_BUTTON,self.OnClickedR3C4) 
      # Box
      Row1BoxR3 = wx.StaticBox(panel, -1, size = ((ColWidth+5)*5,RowWidth-5), pos = (Col1,Row3-5))
      # Checkboxes
      self.cbR3C2 = wx.CheckBox(panel, -1, label = "", pos = (Col2 + ButtonWidth+5,Row3))
      self.cbR3C3 = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row3))
      self.cbR3C4 = wx.CheckBox(panel, -1, label = "", pos = (Col4 + ButtonWidth+5,Row3))

      
      self.Centre() 
      self.Show() 
      self.Fit()  
      
   # Row 1 Functions   
   def OnClickedR1C2(self, event): 
      btnR1C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C2Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR1C2.SetValue(True)
      
   def OnClickedR1C3(self, event): 
      btnR1C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C3Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR1C3.SetValue(True)
      
   def OnClickedR1C4(self, event): 
      btnR1C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR1C4Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR1C4.SetValue(True)      

   # Row 2 Functions   
   def OnClickedR2C2(self, event): 
      btnR2C2Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR2C2Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
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
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR3C2.SetValue(True)
      
   def OnClickedR3C3(self, event): 
      btnR3C3Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C3Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR3C3.SetValue(True)
      
   def OnClickedR3C4(self, event): 
      btnR3C4Label = event.GetEventObject().GetLabel() 
      print("Label of pressed button = %s"%(btnR3C4Label))
      #core.shellCall([sys.executable, "FRTPsychopyFiles/FRTDemo_GUI.py", self.PartID.GetValue()])
      self.cbR3C4.SetValue(True)  
      
app = wx.App() 
Mywin(None,  'NCM Lab') 
app.MainLoop()
