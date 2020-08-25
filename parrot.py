try:
	name=input ("您怎么称呼？")
	print ("你好，"+name+"!")
	from random import randint
	from os import system
	a=randint(0,7)
	if a==0:
		system ("parrot___")
	elif a==1:
		system ("cities")
	elif a==2:
		system ("things")
	elif a==3:
		system ("a")
	elif a==4:
		system ("mountain")
	elif a==5:
		system ("eat")
	elif a==6:
		system("color")
	elif a==7:
		system("number")
except:
	print("\a")

	
	
