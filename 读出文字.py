from tkinter import *
try:
	from tkinter.scrolledtext import ScrolledText
	def say_message():
		import pyttsx3
		engine=pyttsx3.init()
		engine.say(message.get())
		engine.runAndWait()
	top=Tk()
	top.title("读出文字")
	top.geometry('500x30')
	label = Label(text='请输入文字：').pack(side=LEFT)
	c=ScrolledText() 
	message=Entry()
	message.pack(side=LEFT,expand=True,fill=X)
	Button(text='朗读',command=say_message).pack(side=RIGHT)
	mainloop()
except:
	pass