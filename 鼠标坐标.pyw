try:
    from tkinter import *

    class App:
        def __init__(self, master):
            self.master = master
            self.initWidgets()

        def initWidgets(self):
            from random import choice
            lb = Label(self.master, width=65, height=23)
            lb.config(bg=choice(['red','yellow','orange','green','lightgreen','blue','cyan','pink','purple']), font=('Times', 20))
            lb.bind('<Motion>', self.motion)
            lb.bind('<B1-Motion>', self.press_motion)
            lb.pack()
            self.show = Label(self.master, width=38, height=1)
            self.show.config(bg='white', font=('Courier New', 20))
            self.show.pack()

        def motion(self, event):
            self.show['text'] = f"鼠标移动到：（{event.x}{event.y}）"
            return

        def press_motion(self, event):
            self.show['text'] = f"按住鼠标的位置为：（{event.x}{event.y}）"
            return

    root = Tk()
    root.title("鼠标坐标")
    root.geometry('1000x750')
    App(root)
    root.mainloop()
except:
    pass
