try:
	from os import system
	from getpass import getuser
	user=getuser()
	while True:
		a=input(user+">")
		system(a)
except:
	pass
