try:
	name=input ("Could I have your name,please?")
	print ("Hello,%s!"%(name))
	del name
	while True:
		from os import system
		from random import randint
		system ("a")
		b=randint (100000,99999999999999999999999999999999999)
		c=input (b)
		if c==b:
			del c,b
			system ("b")
		else:
			del c,b
			system ("c")
except:
	system ("d")