try:
	from os import system
	name=input("您怎么称呼？")
	print("你好，%s！"%(name))
	print("%s，颜色属性由两个十六进制数字指定 -- 第一个对应于背景，第二个对应于前景。注意，只能大写。每个数字可以为以下任何值:"%(name))
	system("a")
	color1=input("背景颜色：")
	color2=input("字体颜色：")
	if color1=='1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or 'A' or 'B' or 'C' or 'D' or 'E' or 'F':
		if color2=='1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or 'A' or 'B' or 'C' or 'D' or 'E' or 'F':
			system("color "+color1+color2+"&& cmd")
			del color1,color2,name
		else:
			system("cmd")
			del color1,color2,name
	else:
		system("cmd")
		del color1,color2,name
except:
	system("cmd")
