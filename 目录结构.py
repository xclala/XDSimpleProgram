try:
    from tkinter import *
    from os import popen
    from tkinter import messagebox
    root = Tk()
    root.title("目录结构")
    root.geometry("1000x750")


    def main_keyboard(event):
        if str(i.get()) == '':
            with popen("tree", "r") as p:
                Label(text=p.read()).pack(side=TOP)
        else:
            with popen("tree "+i.get(), "r") as p:
                Label(text=p.read()).pack(side=TOP)


    def main():
        if str(i.get()) == '':
            with popen("tree", "r") as p:
                Label(text=p.read()).pack(side=TOP)
        else:
            with popen("tree "+i.get(), "r") as p:
                Label(text=p.read()).pack(side=TOP)
    def on_closing():
        if messagebox.askokcancel("退出", "你确定要退出吗？"):
            root.destroy()


    def on_closing_keyboard(event):
        if messagebox.askokcancel("退出", "你确定要退出吗？"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    i = Entry(width=100,font=40)
    i.pack(side=TOP)
    root.bind("<Return>",main_keyboard)
    root.bind("Alt+F4",on_closing_keyboard)
    Button(text='显示',command=main).pack()
    mainloop()
except:
    pass