from os import system
system ("a")
try:
	name=input ("Could I have your name,please?")
	print ("Hi,"+name)
	while True:
			path=input ("path:")
			c="pyinstaller -D "
			d=c+path
			system (d)
except:
	pass 
		 
		
