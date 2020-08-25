while True:
	try:
		import os
		os.system ("cities_a")
		a=input ("(完成后输入'ctrl+z'或者'ctrl+c'。)")
		b=input ("你喜欢干这件事吗？(0/1)")
		if b=='0':
			print ("我也讨厌"+a+"！")
		elif b=='1':
			print ("我也喜欢"+a+"！")
		else:
			print ("\a")
			os.system ("cities__b")
	except:
	    break


	
    
