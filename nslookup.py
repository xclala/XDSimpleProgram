try:
	while True:
		targetIP=input("targetIP:")
		from os import system
		system("nslookup %s"%(targetIP))
		del targetIP
except:
	pass