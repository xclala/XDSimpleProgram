from tkinter import colorchooser
from tkinter.messagebox import showinfo,askokcancel
from tkinter import *


def cc():
    showinfo(title="颜色", message=colorchooser.askcolor(title="颜色选择"))


root = Tk()
root.title("颜色选择器")
root.geometry("230x30")

def on_closing():
    if messagebox.askokcancel("退出", "你确定要退出吗？"):
        root.destroy()
Button(root, text="选择颜色", command=cc).pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
