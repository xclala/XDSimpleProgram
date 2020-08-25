try:
	a=input ("您怎么称呼？")
	print ("你好"+a+"!")
	while True:
		b=input ("您要检测哪个数字？")
		c=input ("您要检测"+b+"能否被哪个数整除？")
		b=int (b)
		c=int (c)
		if b%c==0:
			b=str (b)
			c=str (c)
			print (a+"，"+b+"能被"+c+"整除。")
		else:
			b=str (b)
			c=str (c)
			print (a+"，"+b+"不能被"+c+"整除。")
except ZeroDivisionError:
	print (a+"，不能说"+b+"能否整除于0。")
except (ValueError,EOFError):
	print (a+"，请输入数字！")
except:
	pass

	
    
