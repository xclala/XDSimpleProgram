try:
	name=input ("Could I have your name,please?")
	print ("Hello,%s!"%(name))
	del name
	while True:
		from os import system
		install=input ("install:")
		system ("c:")
		install="pip install "+install
		system(install)
		system ("a")
		print()
		system("pip list")
except:
	print("\a") 
