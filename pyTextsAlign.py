#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx

MAIN_WIDTH = 500

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        # self.dirname=''
        self.all_ready=False

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(MAIN_WIDTH, 500))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        # menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open files to align")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        # self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.comboBox = wx.ComboBox(self, -1, "Simple Alignment", (MAIN_WIDTH - 200, 0), wx.DefaultSize, ["Naive Alignment", "Simple Alignment", "Hunalign"], wx.CB_DROPDOWN)

        # TODO: Choose files paths.

        # self.fltextFile = 

        # self.sltextFile = 

        # TODO: Add align button.

        # TODO: In each row add more columns, etc.

        self.control = wx.BoxSizer(wx.VERTICAL)
        for col in range(3):
            bw = wx.Button(self, label=str(col + 1))
            self.control.Add(bw)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.comboBox, 0, wx.EXPAND)
        # self.sizer.Add(self.fltextFile, 1, wx.EXPAND)
        # self.sizer.Add(self.sltextFile, 2, wx.EXPAND)
        self.sizer.Add(self.control, 3, wx.EXPAND)

        # TODO: Add save button.

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " Texts aligner ", "About pyTextsAlign", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    # def OnOpen(self,e):
    #     """ Open a file"""
    #     dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
    #     if dlg.ShowModal() == wx.ID_OK:
    #         self.filename = dlg.GetFilename()
    #         self.dirname = dlg.GetDirectory()
    #         f = open(os.path.join(self.dirname, self.filename), 'r')
    #         self.control.SetValue(f.read())
    #         f.close()
    #     dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "pyTextsAlign")
app.MainLoop()
