#pyinstaller -F -w 颜色选择器.py
from tkinter import colorchooser
from tkinter.messagebox import showinfo
from tkinter import *


def cc():
    showinfo(title="颜色",message=colorchooser.askcolor(title="颜色选择"))


root = Tk()
root.title("颜色选择器")
root.geometry("230x30")
button = Button(root, text="选择颜色", command=cc).pack()
root.mainloop()
