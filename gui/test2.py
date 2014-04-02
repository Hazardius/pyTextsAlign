#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkMessageBox
import Tkinter
from Tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)
text = Text(canvas, height =1, width = 5 )
text.insert(INSERT, "Tekst")
text.pack()
root.mainloop()
