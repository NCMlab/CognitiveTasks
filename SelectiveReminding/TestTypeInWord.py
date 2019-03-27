import wx
count = 1
app = wx.App()

frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)

# Create text input
dlg = wx.TextEntryDialog(frame, 'Enter Intrusion %d'%(count),'Text Entry')
# dlg.SetValue("Default")
if dlg.ShowModal() == wx.ID_OK:
    print('You entered: %s\n' % dlg.GetValue())
dlg.Destroy()