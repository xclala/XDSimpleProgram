try:
    from tkinter import *
    root = Tk()
    root.attributes('-fullscreen', True)
    root.wm_attributes('-topmost', True)
    Frame(root, bg='white').pack(fill='both', expand=True)
    mainloop()
except:
    pass
