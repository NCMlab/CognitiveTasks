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
RowWidth = 30
ColWidth = 100
# Button height cannot be changed
ButtonHeight = -1
ButtonWidth = 80
Row1 = Top 
Row2 = Top + RowWidth
Row3 = Top + 2*RowWidth

Col1 = Left
Col2 = Left + ColWidth
Col3 = Left + 2*ColWidth

class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (600,600))  
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col1,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col2,Row1), size = ((ButtonWidth, ButtonHeight))) 
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col3,Row1), size = ((ButtonWidth, ButtonHeight))) 
      Row1Box = wx.StaticBox(panel, -1, size = ((ColWidth+5)*3,RowWidth+5), pos = (Col1,Row1-5))
      Row1Box = wx.StaticBox(panel, -1, size = ((ColWidth+5)*3,RowWidth+5), pos = (Col1,Row2-5))
      Row1Box = wx.StaticBox(panel, -1, size = ((ColWidth+5)*3,RowWidth+5), pos = (Col1,Row3-5))
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col1,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col2,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.btn = wx.Button(panel,-1,"Demo", pos = (Col3,Row2), size = ((ButtonWidth, ButtonHeight))) 
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col1 + ButtonWidth+5,Row1))
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col2 + ButtonWidth+5,Row1))
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row1))
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col1 + ButtonWidth+5,Row2))
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col2 + ButtonWidth+5,Row2))
      self.cb = wx.CheckBox(panel, -1, label = "", pos = (Col3 + ButtonWidth+5,Row2))
      self.Centre() 
      self.Show() 
      self.Fit()  
app = wx.App() 
Mywin(None,  'NCM Lab') 
app.MainLoop()

#
#Row2
#Row3
#Row4
#Col1
#Col2
#Col3