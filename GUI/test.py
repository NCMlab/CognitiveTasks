
from psychopy import gui
import numpy as np

def TypeInNumbers(): 
    # When [intrusion] is clicked on teh screen by the tester, this fn will
    # present a dialog box for the intusion word to be types in
    print('Entered Intrusion Entry')
    app = gui.wx.PySimpleApp()
    
    frame = gui.wx.Frame(None, -1, 'win.py')
    frame.SetDimensions(0,0,200,50)
    
    # Create text input
    dlg = gui.wx.TextEntryDialog(frame, 'Type in number list','Text Entry')
    # dlg.SetValue("Default")
    if dlg.ShowModal() == gui.wx.ID_OK:
        print('You entered: %s\n' % dlg.GetValue())
    dlg.Destroy()
    response = dlg.GetValue()
    # remove non numerics from the string
    response = ''.join(c for c in response if c.isdigit())
    return response


response = TypeInNumbers()
print(response)
RespList = []
for i in response:
    RespList.append(int(i))
RespList = np.array(RespList)
print(RespList)