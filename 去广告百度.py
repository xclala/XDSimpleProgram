from tkinter import *
try:
    from tkinter.scrolledtext import ScrolledText
    def search():
        from webbrowser import open
        open('https://www.baidu.com/s?wd='+wangzhi.get()+' -推广 -广告')

    def setting_button():
        Button(text=m.get(), command=search,bg='black',fg='white').pack(side=RIGHT)
    top = Tk()
    top.title("浏览器")
    top.geometry('1500x30')
    wangzhi = Entry()
    m = Entry(bg='black', fg='white')
    Label(text='请输入关键字：').pack(side=LEFT)
    wangzhi.pack(side=LEFT, expand=True, fill=X)
    Label(text='请输入临时收藏名：', bg='black', fg='white').pack(side=LEFT)
    m.pack(side=LEFT, expand=True, fill=X)
    Button(text='临时收藏', command=setting_button, bg='black',
           fg='white').pack(side=RIGHT)
    Button(text='百度一下', command=search).pack(side=RIGHT)
    mainloop()
except:
    pass