try:
    from tkinter import *
    root = Tk()
    root.title("恶作剧")
    root.geometry('210x30')

    def bluescreen():
        from os import system
        system("bluescreen")

    def whitescreen():
        from os import system
        system("whitescreen")

    def redscreen():
        from os import system
        system("redscreen")

    def blackscreen():
        from os import system
        system("blackscreen")

    def yellowscreen():
        from os import system
        system("yellowscreen")

    def greenscreen():
        from os import system
        system("greenscreen")
    Button(text='蓝屏', command=bluescreen).pack(side=LEFT)
    Button(text='黑屏', command=blackscreen).pack(side=LEFT)
    Button(text='红屏', command=redscreen).pack(side=LEFT)
    Button(text='白屏', command=whitescreen).pack(side=LEFT)
    Button(text='黄屏', command=yellowscreen).pack(side=LEFT)
    Button(text='绿屏', command=greenscreen).pack(side=LEFT)
    mainloop()
except:
    pass
