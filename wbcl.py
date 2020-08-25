try:
	import codecs
	name=input("您怎么称呼？")
	while name=='' or name=='*':
		from os import system
		system("文本处理")
	else:
		print("你好，%s！"%(name))
		print("%s，欢迎使用本程序！"%(name))
		a=input("%s，替换“文本处理.txt”的全部内容的，输入“r”；统计“文本处理.txt”的字数的，输入“s”；从“文本处理.txt”中查找是否有某一内容的，输入“f”。"%(name))
		if a=='r' or a=='R':
			message_r=input("%s，您要替换的字符是什么？"%(name))
			with open('文本处理.txt','w') as file_object:
				file_object.write(message_r)
			del message_r
			print("%s，正在替换。。。"%(name))
			print("%s，替换成功！"%(name))
		elif a=='s' or a=='S':
			with open('文本处理.txt') as file_object:
				file_object=codecs.open('文本处理.txt','r+',encoding='utf-8')
				words=file_object.read()
				number_words=len(words)
				del words
				number_words=str(number_words)
			print(name+"，一共有"+number_words+"字。")
			del number_words
		elif a=='f' or a=='F':
			from re import compile,search
			message_f=input("%s，您要查找的是什么内容？"%(name))
			p=compile(message_f)
			with open('文本处理.txt') as file_object2:
				file_object2=codecs.open('文本处理.txt','r+',encoding='utf-8')
				f=file_object2.read()
			b=p.search(f)
			del f,p
			if b:
				print("%s，含有内容。"%(name))
			else:
				print("%s，不含有内容。"%(name))
		del a
		print("%s，谢谢使用本程序！"%(name))
		input("%s，请按任意键继续。"%(name))
		del name
except:
	pass
