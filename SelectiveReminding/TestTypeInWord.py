from psychopy import gui
count = 1
app = gui.wx.App()

frame = gui.wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)

# Create text input
dlg = gui.wx.TextEntryDialog(frame, 'Enter Intrusion %d'%(count),'Text Entry')
# dlg.SetValue("Default")
if dlg.ShowModal() == gui.wx.ID_OK:
    print('You entered: %s\n' % dlg.GetValue())
dlg.Destroy()


