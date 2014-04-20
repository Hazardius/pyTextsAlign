import wx

labels = "1 2 3 4 5 6 7 8 9 0".split()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "GridBagSizer Test")
        sizer = wx.GridBagSizer(hgap=5, vgap=5)
        for col in range(3):
            for row in range(3):
                bw = wx.Button(self, label=labels[row*3 + col])
                sizer.Add(bw, pos=(row,col))

        bw = wx.Button(self, label="span 3 rows")
        sizer.Add(bw, pos=(0,3), span=(3,1), flag=wx.EXPAND)

        bw = wx.Button(self, label="span all columns")
        sizer.Add(bw, pos=(3,0), span=(1,4), flag=wx.EXPAND)

        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)

        self.SetSizer(sizer)
        self.Fit()
        

app = wx.PySimpleApp()
TestFrame().Show()

app.MainLoop()
