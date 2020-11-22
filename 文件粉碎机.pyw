from tkinter import *
from tkinter import messagebox
try:
	from tkinter.scrolledtext import ScrolledText
	def main():
		from os import remove,system
		remove(filename.get())
		with open(filename.get(),'w',encoding='utf-8') as file:
			file.write("")
		remove(filename.get())
	def on_closing():
		if messagebox.askokcancel("退出", "你确定要退出吗？"):
			top.destroy()
	top=Tk()
	top.title("文件粉碎机")
	top.geometry('1500x30')
	Label(text='请输入文件名：').pack(side=LEFT)
	c=ScrolledText()
	filename=Entry()
	filename.pack(side=LEFT,expand=True,fill=X)
	Button(text='粉碎',command=main).pack(side=RIGHT)
	top.protocol("WM_DELETE_WINDOW", on_closing)
	mainloop()
except:
	pass
		

	
    
