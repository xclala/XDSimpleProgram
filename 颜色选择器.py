#pyinstaller -F 颜色选择器.py
from tkinter import colorchooser
from tkinter import *


def cc():
    print(colorchooser.askcolor(title="颜色选择"))


root = Tk()
root.title("颜色选择器")
root.geometry("230x30")
button = Button(root, text="选择颜色", command=cc).pack()
root.mainloop()
