try:
    from tkinter import *
    import tkinter
    from tkinter. scrolledtext import ScrolledText
    root=Tk()
    def run():
        print(exec(contents.get('1.0', END)))
        root.title("RUNNING")
    def load_and_run():
        with open(filename.get(),encoding='utf-8') as file:
            print(exec(file.read()))
        root.title("RUNNING "+filename.get())
    def path():
        from os import getcwd
        Label(text=getcwd(),bg=filename.get()).pack(side=LEFT)
    def start():
        from os import system
        system("SimplePython3Shell")
    root.title("simple python3 shell")
    root.geometry('1500x630')
    contents=ScrolledText(font=40).pack(side=BOTTOM,expand=True,fill=BOTH)
    filename=Entry().pack(side=LEFT,expand=True,fill=X)
    Button(text='Show path',command=path).pack(side=RIGHT)
    Button(text='Start a new window',command=start).pack(side=RIGHT)
    Button(text='Run',command=run).pack(side=RIGHT)
    mainloop()
except Exception as e:
    print(e+"\a")
    
