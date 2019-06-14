import wx
app = wx.App()
dlg = wx.DirDialog(None, "Choose data output directory", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
if dlg.ShowModal() == wx.ID_OK:
    print(dlg.GetPath())
dlg.Destroy()    
