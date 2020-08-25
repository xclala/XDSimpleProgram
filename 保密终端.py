try:
	from os import system
	from getpass import getpass
	while True:
		a=getpass(">")
		system(a)
except:
	pass