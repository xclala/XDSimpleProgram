from tkinter import *
from tkinter import messagebox
try:
    from tkinter.scrolledtext import ScrolledText


    def search():
        import wx
        from wx.html2 import WebView

        class MAIN(wx.Frame):
            def __init__(self, parent, title):
                wx.Frame.__init__(self, parent, -1, title, size=(1000, 800))
                WebView.New(self).LoadURL(wangzhi.get())

        app = wx.App()
        frm = MAIN(None, wangzhi.get())
        frm.Show()
        app.MainLoop()


    def qrcode():
        from MyQR.myqr import run
        from os import getcwd
        run(words=wangzhi.get())


    def setting_button():
        Button(text=m.get(), command=search).pack(side=RIGHT)

    def on_closing():
        if messagebox.askokcancel("退出", "你确定要退出吗？"):
            top.destroy()
    top = Tk()
    top.title("浏览器")
    top.geometry('1500x30')
    top.protocol("WM_DELETE_WINDOW", on_closing)
    wangzhi = Entry()
    m = Entry(bg='black', fg='white')
    Label(text='网址：').pack(side=LEFT)
    wangzhi.pack(side=LEFT, expand=True, fill=X)
    Label(text='临时收藏名：', bg='black', fg='white').pack(side=LEFT)
    m.pack(side=LEFT, expand=True, fill=X)
    Button(text='生成二维码', command=qrcode, bg='green', fg='white').pack(side=RIGHT)
    Button(text='临时收藏', command=setting_button, bg='black',
           fg='white').pack(side=RIGHT)
    Button(text='搜索', command=search).pack(side=RIGHT)
    mainloop()
except:
    pass
