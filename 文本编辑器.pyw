try:
    from tkinter import *
    from tkinter.scrolledtext import ScrolledText

    top = Tk()


    def load():
        with open(filename.get()) as file:
            contents.delete('1.0', END)
            contents.insert(INSERT, file.read())


    def save():
        with open(filename.get(), 'w') as file:
            file.write(contents.get('1.0', END))


    def quit():
        top.quit()


    def a_new_window():
        from os import system
        system("python 文本编辑器.pyw")


    top.title("Editor(文本编辑器）")
    contents = ScrolledText()
    contents.pack(side=BOTTOM, expand=True, fill=BOTH)
    filename = Entry()
    filename.pack(side=LEFT, expand=True, fill=X)
    Button(text='Open(打开)', command=load).pack(side=LEFT)
    Button(text='Save(保存)', command=save).pack(side=LEFT)
    Button(text='Quit(退出)', command=quit).pack(side=LEFT)
    Button(text='A New Window(新窗口)', command=a_new_window).pack(side=LEFT)
    mainloop()
except:
    pass
