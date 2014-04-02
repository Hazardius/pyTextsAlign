#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkMessageBox
import Tkinter
from Tkinter import *
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def addtext(packframe, packframe2):
   var = StringVar()
   label = Message( packframe, text="Zdanie po polsku", relief=RAISED )
   label.pack()
   label2 = Message( packframe2, text="Zdanie po angielsku", relief=RAISED )
   label2.pack()
   return

WINDOW_SIZE_HEIGHT = 400
WINDOW_SIZE_WIGHT = 500
root = Tkinter.Tk()
frame = Frame(root, height=WINDOW_SIZE_HEIGHT, width=WINDOW_SIZE_WIGHT)

frame.pack(side=LEFT, fill=BOTH, expand=TRUE)
canvas = Tkinter.Canvas(frame, bg="green", height=7000, width=WINDOW_SIZE_WIGHT, scrollregion=(0,0,200,700))
scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side = RIGHT, fill =Y)
canvas.pack(side=LEFT)
canvas.config(height=WINDOW_SIZE_HEIGHT, width=WINDOW_SIZE_WIGHT)
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.config( command = canvas.yview )



packframe = Frame(canvas, bg="blue", height=1000, width=WINDOW_SIZE_WIGHT/2)

packframe.pack(side=LEFT)

packframe2 = Frame(canvas, bg="red", width=WINDOW_SIZE_WIGHT/2)
packframe2.pack(side=RIGHT)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
addtext(packframe, packframe2)
#w = PanedWindow( root, bg ="red" )
#w.pack(fill=BOTH, expand=1)
root.mainloop()
