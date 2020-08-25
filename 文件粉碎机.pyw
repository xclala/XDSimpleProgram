from tkinter import *
try:
	from tkinter.scrolledtext import ScrolledText
	def main():
		from os import remove,system
		remove(filename.get())
		with open(filename.get(),'w',encoding='utf-8') as file:
			file.write("")
		remove(filename.get())
	top=Tk()
	top.title("文件粉碎机")
	top.geometry('1500x30')
	Label(text='请输入文件名：').pack(side=LEFT)
	c=ScrolledText()
	filename=Entry()
	filename.pack(side=LEFT,expand=True,fill=X)
	Button(text='粉碎',command=main).pack(side=RIGHT)
	mainloop()
except:
	pass
		

	
    
