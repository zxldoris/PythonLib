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
t = Text(frame)  # 此处可以设置为Entry小部件，注意在key函数中，.insert(index,opt),index参数改变
root.mainloop()

"""""""""""""""""""""""""""""""""""""""""""""
以下是类写法
"""""""""""""""""""""""""""""""""""""""""""""

# class Opt(object):
#     def __init__(self):
#         self.root = tkinter.Tk()
#         self.frame = tkinter.Frame(self.root, width=300, height=20)
#         self.frame.pack(side='bottom')
#         self.root_canvas = tkinter.Canvas(self.root,
#                                           width=300, height=400, bg='white')
#         self.root_canvas.pack(side='top')
#         # 创建文本输入框 并放到frame上
#         self.e = tkinter.Entry(self.frame)
#
#     def main_opt(self):
#         self.frame.bind("<Key>", self.__key)
#         self.frame.bind("<Button-1>", self.__callback)
#         self.root.mainloop()
#
#     def __key(self, event):
#         self.e.pack()
#         print("pressed", repr(event.char))
#         self.e.insert(1, repr(event.char))
#         return repr(event.char)  # 返回键盘输入数据
#
#     def __callback(self, event):
#         self.frame.focus_set()
#         print("clicked at", event.x, event.y)