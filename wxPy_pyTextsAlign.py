#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx

from pta_alignment import alignment, atype
from pta_files import open_file

MAIN_WIDTH = 500

class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        self.alignment = None
        self.dirname='' # Used to contain last opened directory.
        self.file1c=None
        self.file2c=None
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

        self.comboBox = wx.Choice(self, -1, choices=["Naive Alignment", "Simple Alignment", "Hunalign"])

        self.fltextFileBut = wx.Button(self, label='Open First File')
        self.lang1ComboBox = wx.Choice(self, -1, choices=['en', 'it', 'pl'])

        self.sltextFileBut = wx.Button(self, label='Open Second File')
        self.lang2ComboBox = wx.Choice(self, -1, choices=['en', 'it', 'pl'])

        self.alignBut = wx.Button(self, label='Align both versions of text')

        # TODO: In each row add more columns, etc.

        self.control = wx.BoxSizer(wx.VERTICAL)
        for col in range(2):
            bw = wx.Button(self, label=str(col + 1))
            self.control.Add(bw)

        self.saveBut = wx.Button(self, label='Save alignment')

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.comboBox, 0, wx.EXPAND)
        self.sizer.Add(self.fltextFileBut, 0, wx.EXPAND)
        self.sizer.Add(self.lang1ComboBox, 0, wx.EXPAND)
        self.sizer.Add(self.sltextFileBut, 0, wx.EXPAND)
        self.sizer.Add(self.lang2ComboBox, 0, wx.EXPAND)
        self.sizer.Add(self.alignBut, 0, wx.EXPAND)
        self.sizer.Add(self.control, 3, wx.EXPAND)
        self.sizer.Add(self.saveBut, 0, wx.EXPAND)

        # Events.
        # self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_BUTTON, self.OpenFile1, self.fltextFileBut)
        self.Bind(wx.EVT_BUTTON, self.OpenFile2, self.sltextFileBut)
        self.Bind(wx.EVT_BUTTON, self.CreateAlignment, self.alignBut)
        self.Bind(wx.EVT_BUTTON, self.SaveAlignment, self.saveBut)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # Deactivation of waiting buttons.
        # self.alignBut.Disable()
        self.saveBut.Disable()

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        # self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " Texts aligner ", "About pyTextsAlign", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OpenFile1(self,e):
        """Open first file."""
        dlg = wx.FileDialog(self, "Choose first file!", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.file1c = os.path.join(self.dirname, self.filename)
        dlg.Destroy()

    def OpenFile2(self,e):
        """Open second file."""
        dlg = wx.FileDialog(self, "Choose second file!", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.file2c = os.path.join(self.dirname, self.filename)
        dlg.Destroy()

    def CreateAlignment(self,e):
        """Create alignment of both versions of the text."""
        self.alignBut.Disable()
        if ((self.file1c != None) and (self.file2c != None)):
            self.fltextFileBut.Disable()
            self.sltextFileBut.Disable()
            at = self._check_atype_()
            self.alignment = alignment(at, (self.file1c, self._check_lang1_()), (self.file2c, self._check_lang2_()))
            self.fltextFileBut.Enable()
            self.sltextFileBut.Enable()
            self.saveBut.Enable()
        self.alignBut.Enable()

    def SaveAlignment(self,e):
        """Save alignment to chosen file."""
        if self.alignment != None:
            dlg = wx.FileDialog(self, "Choose save file!", self.dirname, "", "*.*", wx.SAVE)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                save_path = os.path.join(self.dirname, self.filename)
                self.alignment.save(save_path)
            dlg.Destroy()

    def _check_atype_(self):
        selected = self.comboBox.GetCurrentSelection()
        if selected == 0:
            return atype.NAIVE
        elif selected == 1:
            return atype.SIMPLE
        elif selected == 2:
            return atype.HUNALIGN

    def _check_lang1_(self):
        selected = self.lang1ComboBox.GetCurrentSelection()
        if selected == 0:
            return 'en'
        elif selected == 1:
            return 'it'
        elif selected == 2:
            return 'pl'

    def _check_lang2_(self):
        selected = self.lang2ComboBox.GetCurrentSelection()
        if selected == 0:
            return 'en'
        elif selected == 1:
            return 'it'
        elif selected == 2:
            return 'pl'

app = wx.App(False)
frame = MainWindow(None, "pyTextsAlign")
app.MainLoop()
