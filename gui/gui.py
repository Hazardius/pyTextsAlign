#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkMessageBox
import Tkinter
from Tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, bg="blue", height=250, width=300)
line = canvas.create_line(150, 0, 150, 250, fill="red")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
text = Text(root, height =1, width = 5 )
text.insert(INSERT, "Tekst")



# Code to add widgets will go here...
canvas.pack()
text.pack()
text.place(bordermode=OUTSIDE, x = 12, y = 5)
w = PanedWindow( root, bg ="red" )
w.pack(fill=BOTH, expand=1)
root.config(menu=menubar)
root.mainloop()

