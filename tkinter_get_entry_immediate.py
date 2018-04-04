#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
描述：
    通过绑定键盘事件和对应处理方法，鼠标左键点击窗口事件，
    实现从键盘输入实时显示在text  widget中。
Version: python3.6
__author__ = 'zxl'
"""
from tkinter import *


def key(event):
    print("pressed", repr(event.char))
    t.insert(1.0, repr(event.char))
    t.pack()


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)


root = Tk()
frame = Frame(root, width=200, height=200)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
t = Text(frame)
root.mainloop()
