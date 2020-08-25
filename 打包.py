from tkinter import *
try:
	from tkinter.scrolledtext import ScrolledText
	from os import system
	def w():
		system("pyinstaller -F -w "+message.get())
	def c():
		system("pyinstaller -F "+message.get())
	top=Tk()
	top.title("打包成exe")
	top.geometry('500x30')
	label = Label(text='请输入python软件名：')
	label.pack(side=LEFT)
	c=ScrolledText()
	message=Entry()
	message.pack(side=LEFT,expand=True,fill=X)
	Button(text='命令行',command=c).pack(side=RIGHT)
	Button(text='可视化',command=w).pack(side=RIGHT)
	mainloop()
except:
	pass