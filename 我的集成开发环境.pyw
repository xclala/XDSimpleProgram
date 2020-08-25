try:
	from tkinter import *
	import tkinter
	from tkinter. scrolledtext import ScrolledText
	from os import system,getcwd
	top = Tk()
	def load(): 
		with open(message.get(),encoding='utf-8') as file:
			contents.delete('1.0', END) 
			contents.insert(INSERT,file.read())
		top.title("打开"+message.get())	
	def save(): 
		with open(message.get(),'w',encoding='utf-8') as file:
			file.write(contents.get('1.0', END))
		top.title("保存"+message.get())
	def python_save():
		with open(message.get()+".py",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0', END))
		top.title("以命令行的python格式保存"+message.get())
	def pythonw_save():
		with open(message.get()+".pyw",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0', END))
		top.title("以可视化的python格式保存"+message.get())
	def c_save():
		with open(message.get()+".c",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以c语言的格式保存")
	def cpp_save():
		with open(message.get()+".cpp",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以c++语言的格式保存")
	def java_save():
		with open(message.get()+".java",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以java语言的格式保存")
	def html_save():
		with open(message.get()+".htm",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以html的格式保存")
	def h_save():
		with open(message.get()+".h",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以c语言头文件的格式保存")
	def bat_save():
		with open(message.get()+".bat",'w',encoding='utf-8') as file:
			file.write(contents.get('1.0',END))
		top.title("以批处理文件的格式保存")
	def pip_install():
		system("pip install "+message.get()+" --no-cache-dir & pause")
		top.title("用pip安装"+message.get())
	def pip_upgrade():
		system("pip install --upgrade "+message.get()+" --no-cache-dir & pause")
		top.title("用pip更新"+message.get())
	def pip_uninstall():
		system("pip uninstall "+message.get()+" --no-cache-dir & pause")
		top.title("用pip卸载"+message.get())
	def pip_install_uninstall():
		system("pip uninstall "+message.get()+" -y & pip install "+message.get()+" --no-cache-dir & pause")
		top.title("用pip重新安装"+message.get())
	def show_all_packages():
		system("pip list & --no-cache-dir & echo ------------------------------------------ & pause")
		top.title("显示安装的所有第三方包")
	def show_upgrade_all_packages():
		system("pip list -o & --no-cache-dir & echo ------------------------------------------ & pause")
		top.title("显示能够更新的所有第三方包")
	def upgrade_all_packages():
		system("pip-review --auto & pause")
		top.title("更新所有第三方包")
	def upgrade_packages():
		system("pip-review --local --interactive & pause")
		top.title("更新第三方包")
	def pip_show():
		system("pip show "+message.get()+" --no-cache-dir & pause")
		top.title(message.get())
	def pip_search():
		system("pip search "+message.get()+" --no-cache-dir & pause")
		top.title(message.get())
	def pip_check():
		system("pip check "+message.get()+" --no-cache-dir & pause")
		top.title(message.get())
	def pip_download():
		system("pip download "+message.get()+" --no-cache-dir & pause")
		top.title("用pip下载"+message.get())
	def start():
		system("python 我的集成开发环境.pyw")
	def python_run():
		system("python "+message.get()+"& echo ------------------ & pause")
		top.title("用python运行"+message.get())
	def c_compile():
		system("gcc -O3 "+message.get()+"& echo ------------------ & pause")
		top.title("编译优化"+message.get())
	def run():
		system(message.get())
		top.title("运行"+message.get())
	def java_compile():
		system("javac "+message.get()+"& echo ------------------ & pause")
		top.title("java编译"+message.get())
	def java_run():
		system("java "+message.get()+"& echo ------------------ & pause")
		top.title("java运行"+message.get())
	def dos():
		system("cmd")
	def python():
		system("python")
	def ipython():
		system("ipython")
	def pyinstaller_exe_c():
		system("pyinstaller -F "+message.get()+"& pause")
		top.title(message.get())
	def pyinstaller_exe_w():
		system("pyinstaller -F -w "+message.get()+"& pause")
		top.title(message.get())
	def liulanqi():
		from webbrowser import open
		open(message.get())
		top.title("浏览"+message.get())
	def calc():
		system("calc")
	def slidetoshutdown():
		system("slidetoshutdown")
	def pythonsetuptools():
		system("python setup.py "+message.get())
		top.title("python用setuptools打包"+message.get())
	def vtenv():
		system("python -m venv "+message.get())
		top.title("python用venv创建虚拟环境"+message.get())
	def hack_ping():
		system("ping -l 65500 "+message.get()+" -t & pause")
		top.title("目标IP:"+message.get())
	def tree():
		system("tree & pause")
		top.title("目录结构")
	def ipython_run():
		system("ipython "+message.get()+"& echo ------------------ & pause")
		top.title("用ipython运行"+message.get())
	def psl():
		system("powershell")
	def c_compile_run():
		system("gcc -O3 "+message.get()+"& a & pause")
		top.title("编译运行c程序"+message.get())
	def java_compile_run():
		system("javac "+message.get()+"& java "+message.get()+".class"+"& pause")
		top.title("编译运行java程序"+message.get())
	def c_i():
		system("gcc -O3 -E "+message.get()+" -o a.i")
		top.title(message.get())
	def c_s_intel():
		system("gcc -O3 -S -masm=intel "+message.get()+" -o a.s")
		top.title("把"+message.get()+"编译成intel的汇编语言")
	def rm():
		from os import remove
		remove(message.get())
		top.title("已永久删除"+message.get())
	def remv():
		top.title("删除"+message.get())
		system("move "+message.get()+" 删除的文件/"+message.get())
	def import_colors():
		system("python colors.pyw")
		top.title("颜色表")
	def pyttsx3_say_messages():
		import pyttsx3
		e=pyttsx3.init()
		e.say(contents.get('1.0', END))
		e.runAndWait()
		top.title("读出文字")
	def pcs():
		system("pycodestyle "+message.get()+"& pause")
		top.title(message.get())
	def pip_shell():
		top.title("交互式pip")
		a=input("pip>")
		system("pip "+a)
		top.title(a)
	def pyinstaller_shell():
		b=input("pyinstaller>")
		system("pyinstaller "+b)
		top.title("交互式pyinstaller")
	def labl():
		lbl=Label(text=message.get())
		lbl.pack(side=LEFT)
	def import_fanyi():
		system("python youdaofanyi.pyw")
		top.title("有道翻译器")
	def pydoc1():
		top.title("python第三方包文档")
		system("python -m pydoc "+message.get()+"& pause")
	def pydoc3():
		top.title("python第三方包文档")
		if message.get()=='':
			system("python -m pydoc -p 80 & pause")
		else:
			system("python -m pydoc -p "+message.get()+"& pause")
	def len_pyttsx3_message():
		import pyttsx3
		f=pyttsx3.init()
		f.say(str(len(contents.get('1.0', END)))+"字")
		f.runAndWait()
		top.title("读出文件字数")
	def tit():
		top.title(message.get())
	def pdb_debug():
		top.title("调试")
		system("python -m pdb "+message.get()+" & pause")
	def ipdb_debug():
		top.title("调试")
		system("python -m ipdb "+message.get()+" & pause")
	def pythoni():
		top.title("运行python程序后运行交互式python")
		system("python -i "+message.get())
	def hide():
		system("attrib +H "+message.get())
	def unhide():
		system("attrib -H "+message.get())
	def path():
		Label(text=getcwd(),bg=message.get()).pack(side=LEFT)
	def serv():
		system("echo 此功能会让同一局域网内的所有用户通过浏览器输入您的ip地址来下载在本目录的文件或打开本目录下的index.html的页面，您可能需要设置防火墙。 & server 80")
	def speed():
		system("py -m cProfile "+message.get()+"& pause")
	def dirdir():
		system("dir /a /q & pause")
	def yapfyapf():
		system("yapf -i "+message.get())
	top.title("我的集成开发环境") 
	top.geometry('1500x630')
	menubar = tkinter.Menu(top)
	contents=ScrolledText(font=40).pack(side=BOTTOM,expand=True,fill=BOTH)
	message=Entry()
	message.pack(side=LEFT,expand=True,fill=X)
	menu1 = tkinter.Menu(menubar, tearoff=False)
	menu1.add_command(label='打开文件',command=load)
	menu1.add_command(label='保存文件',command=save)
	menu1.add_command(label='隐藏文件',command=hide)
	menu1.add_command(label='恢复隐藏的文件',command=unhide)
	menu1.add_command(label='以命令行的python格式保存文件(.py)',command=python_save)
	menu1.add_command(label='以可视化的python格式保存文件(.pyw)',command=pythonw_save)
	menu1.add_command(label='以c语言的格式保存(.c)',command=c_save)
	menu1.add_command(label='以c++语言的格式保存(.cpp)',command=cpp_save)
	menu1.add_command(label='以java语言的格式保存(.java)',command=java_save)
	menu1.add_command(label='以html的格式保存(.htm)',command=html_save)
	menu1.add_command(label='以c语言头文件的格式保存(.h)',command=h_save)
	menu1.add_command(label='以批处理文件的格式保存(.bat)',command=bat_save)
	menu1.add_command(label='删除文件',command=remv)
	menu1.add_command(label='永久删除文件',command=rm)
	menubar.add_cascade(label="文本编辑", menu=menu1)
	top.config(menu=menubar)
	menu2 = tkinter.Menu(menubar, tearoff=False)
	menu2.add_command(label='提供可选项更新第三方包',command=upgrade_packages)
	menu2.add_command(label='更新所有第三方包',command=upgrade_all_packages)
	menu2.add_command(label='显示能够更新的所有第三方包',command=show_upgrade_all_packages)
	menu2.add_command(label='显示安装的所有第三方包',command=show_all_packages)
	menu2.add_command(label='检查依赖',command=pip_check)
	menu2.add_command(label='搜索',command=pip_search)
	menu2.add_command(label='查看信息',command=pip_show)
	menu2.add_command(label='下载安装包',command=pip_download)
	menu2.add_command(label='卸载',command=pip_uninstall)
	menu2.add_command(label='重新安装',command=pip_install_uninstall)
	menu2.add_command(label='更新',command=pip_upgrade)
	menu2.add_command(label='安装',command=pip_install)
	menubar.add_cascade(label="python第三方包软件商店", menu=menu2)
	top.config(menu=menubar)
	menu3 = tkinter.Menu(menubar, tearoff=False)
	menu3.add_command(label='运行python程序',command=python_run)
	menu3.add_command(label='用ipython运行python程序',command=ipython_run)
	menu3.add_command(label='运行python程序后运行交互式python',command=pythoni)
	menu3.add_command(label='编译c程序',command=c_compile)
	menu3.add_command(label='预处理c程序',command=c_i)
	menu3.add_command(label='编译c程序成汇编语言',command=c_s_intel)
	menu3.add_command(label='运行.exe或.bat程序',command=run)
	menu3.add_command(label='编译运行c程序',command=c_compile_run)
	menu3.add_command(label='编译java程序',command=java_compile)
	menu3.add_command(label='运行java程序',command=java_run)
	menu3.add_command(label='编译运行java程序',command=java_compile_run)
	menubar.add_cascade(label="编译与运行", menu=menu3)
	top.config(menu=menubar)
	menu4 = tkinter.Menu(menubar, tearoff=False)
	menu4.add_command(label='dos',command=dos)
	menu4.add_command(label='python',command=python)
	menu4.add_command(label='ipython',command=ipython)
	menu4.add_command(label='powershell',command=psl)
	menu4.add_command(label='交互式pip',command=pip_shell)
	menu4.add_command(label='交互式pyinstaller',command=pyinstaller_shell)
	menubar.add_cascade(label="命令行", menu=menu4)
	top.config(menu=menubar)
	menu5 = tkinter.Menu(menubar, tearoff=False)
	menu5.add_command(label='把python程序编译成命令行的exe',command=pyinstaller_exe_c)
	menu5.add_command(label='把python程序编译成可视化的exe',command=pyinstaller_exe_w)
	menubar.add_cascade(label="把python程序编译成exe", menu=menu5)
	top.config(menu=menubar)
	menu6 = tkinter.Menu(menubar, tearoff=False)
	menu6.add_command(label='命令行',command=pydoc1)
	menu6.add_command(label='所有第三方包的网页版',command=pydoc3)
	menubar.add_cascade(label="第三方包文档", menu=menu6)
	top.config(menu=menubar)
	menu7 = tkinter.Menu(menubar, tearoff=False)
	menu7.add_command(label='读出文字',command=pyttsx3_say_messages)
	menu7.add_command(label='读出文件字数',command=len_pyttsx3_message)
	menubar.add_cascade(label='朗读',menu=menu7)
	top.config(menu=menubar)
	menu8 = tkinter.Menu(menubar, tearoff=False)
	menu8.add_command(label='显示运行速度',command=speed)
	menu8.add_command(label='用pdb调试',command=pdb_debug)
	menu8.add_command(label='用ipdb调试',command=ipdb_debug)
	menubar.add_cascade(label='python调试',menu=menu8)
	top.config(menu=menubar)
	menu9=tkinter.Menu(menubar,tearoff=False)
	menu9.add_command(label='修改标题',command=tit)
	menu9.add_command(label='显示路径',command=path)
	menubar.add_cascade(label='设置',menu=menu9)
	top.config(menu=menubar)
	menu10=tkinter.Menu(menubar,tearoff=False)
	menu10.add_command(label='显示目录下的文件',command=dirdir)
	menu10.add_command(label='显示目录结构',command=tree)
	menubar.add_cascade(label='显示目录',menu=menu10)
	top.config(menu=menubar)
	menu11=tkinter.Menu(menubar,tearoff=False)
	menu11.add_command(label='检查python程序规范',command=pcs)
	menu11.add_command(label='把python代码修改成规范的样子',command=yapfyapf)
	menubar.add_cascade(label='python代码规范',menu=menu11)
	top.config(menu=menubar)
	Button(text='再启动一个窗口',command=start).pack(side=RIGHT)
	Button(text='滑动关机',command=slidetoshutdown).pack(side=RIGHT)
	Button(text='浏览器',command=liulanqi).pack(side=RIGHT)
	Button(text='计算器',command=calc).pack(side=RIGHT)
	Button(text='添加到任务栏',command=labl).pack(side=RIGHT)
	Button(text='检查python程序规范',command=pcs).pack(side=RIGHT)
	Button(text='死亡之ping',command=hack_ping).pack(side=RIGHT)
	Button(text='有道翻译器',command=import_fanyi).pack(side=RIGHT)
	Button(text='创建虚拟环境',command=vtenv).pack(side=RIGHT)
	Button(text='用setuptools打包(需先填写setup.py)',command=pythonsetuptools).pack(side=RIGHT)
	Button(text='目录结构',command=tree).pack(side=RIGHT)
	Button(text='颜色表',command=import_colors).pack(side=RIGHT)
	Button(text='通过网页显示',command=serv).pack(side=RIGHT)
	mainloop()
except:
	pass
 