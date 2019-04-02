from psychopy import gui


Top = 20
Left = 20
RowWidth = 50
ColWidth = 100
# Button height cannot be changed
ButtonHeight = -1
ButtonWidth = 80
LabelOffset = 10
# Allow flexible number of rows
NRows =  12
# Create a list of what pixel each row is to be set to
RowPixel = []
for i in range(NRows):
    RowPixel.append(Top + i*RowWidth)
# Use the number of rows to define the GUI height
GUIHeight = max(RowPixel) + RowWidth
# Allow flexible number of columns
NCols =  7
# Create a list of what pixel each row is to be set to
ColPixel = []
for i in range(NCols):
    ColPixel.append(Top + i*ColWidth)
# Use the number of rows to define the GUI height
GUIWidth = max(ColPixel) + 2*ColWidth
NColForBox = NCols

class Mywin(gui.wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (GUIWidth,GUIHeight))  
      self.panel = gui.wx.Panel(self) 
      vbox = gui.wx.BoxSizer(gui.wx.VERTICAL) 
      
       # STROOP
      CurrentRow = RowPixel[1]
      self.title1 = gui.wx.StaticText(self.panel, -1, label = "Stroop", pos = (ColPixel[0]+LabelOffset/2,CurrentRow+LabelOffset))
      # Buttons
      self.btnR1C2 = gui.wx.Button(self.panel,-1,"Color", pos = (ColPixel[1],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
#      self.btnR1C2.Bind(gui.wx.EVT_BUTTON,self.OnClickedR1C2) 
      self.btnR1C3 = gui.wx.Button(self.panel,-1,"Word", pos = (ColPixel[2],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      #self.btnR1C3.Bind(gui.wx.EVT_BUTTON,self.OnClickedR1C3) 
      self.btnR1C4 = gui.wx.Button(self.panel,-1,"ColorWord", pos = (ColPixel[3],CurrentRow), size = ((ButtonWidth, ButtonHeight))) 
      #self.btnR1C4.Bind(gui.wx.EVT_BUTTON,self.OnClickedR1C4)
   
      
      
      
      self.Centre() 
      self.Show() 
      self.Fit()     
      
app = gui.wx.App() 
# Create the GUI
MyGui = Mywin(None,  'NCM Lab') 
# Disable all the buttons except the Part ID entry 
MyGui.Disable()
app.MainLoop()