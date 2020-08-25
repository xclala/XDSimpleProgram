from tkinter import *
try:
	from tkinter.scrolledtext import ScrolledText
	from os import system
	def pip_install():
		system("pip install "+message.get())
	def pip_upgrade():
		system("pip install --upgrade "+message.get())
	def pip_uninstall():
		system("pip uninstall "+message.get())
	def terminal():
		system("cmd")
	top=Tk()
	top.title("读出文字")
	top.geometry('500x30')
	label = Label(text='请输入第三方包名：')
	label.pack(side=LEFT)
	c=ScrolledText()
	message=Entry()
	message.pack(side=LEFT,expand=True,fill=X)
	Button(text='卸载',command=pip_uninstall).pack(side=RIGHT)
	Button(text='更新',command=pip_upgrade).pack(side=RIGHT)
	Button(text='下载',command=pip_install).pack(side=RIGHT)
	Button(text='终端',command=terminal).pack(side=RIGHT)
	mainloop()
except:
	pass