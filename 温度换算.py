try:
	a=input ("Could I have your name,please?")
	print ("Hello,"+a)
	c=int(input (a+",c="))
	e=c*8/7
	d=c+273.15
	c=str (c)
	e=str(e)
	d=str(d)
	print (a+","+c+"c="+e+"f")
	print (a+","+c+"c="+d+"K")
	input ()
except (ValueError,EOFError):
	import os
	print ("\a")
	os.system ("huansuan_")
	input ()

