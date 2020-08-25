while True:
	try:
		from os import system
		system ("eat_")
		a=input ("（完成后输入（“ctrl+z”或“ctrl+c”。）")
		b=input ("你喜欢吃"+a+"吗？(0/1)")
		input("为什么？")
		if b=='0':
			print ("我也不喜欢吃"+a+"!")
		elif b=='1':
			print ("我也喜欢吃"+a+"!")
		else:
			print("\a")
	except:
		break
		print("\a")
