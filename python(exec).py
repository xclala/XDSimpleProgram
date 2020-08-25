try:
	from os import system
	system ("a")
	while True:
		a=input("<<<")
		if a=='quit()':
			break
		else:
			exec(a)
except Exception as e:
	print ("\a")
	print (e)
	import python 