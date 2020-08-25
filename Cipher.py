try:
	from os import system
	name=input ("Could I have your name,please?")
	print ("Hello,"+name+"!")
	MAX_KEY_SIZE=(25)
	def getMode():
		while True:
			system ("a")
			mode=input().lower()
			if mode in "encrypt e decrypt d brute b".split():
				return mode[0]
			else:
				system ("b")
	def getMessage():
		system ("c")
		return input()
	def getKey():
		key=0
		while True:
			print ("Enter the key number (1-%s)"% (MAX_KEY_SIZE))
			key=int(input())
			if (key > 0 and key <= MAX_KEY_SIZE):
				return key
	def getTranslatedMessage(mode,message,key):
		if mode[0]=='d':
			key=-key
		translated=""
		for symbol in message:
			if symbol.isalpha():
				num=ord (symbol)
				num+=key
				if symbol.isupper():
					if num>ord("Z"):
						num-=26
					elif num<ord ("A"):
						num+=26
				elif symbol.islower():
					if num>ord("z"):
						num-=26
					elif num<ord("a"):
						num+=26
				translated+=chr (num)
			else:
				translated+=symbol
		return translated
	mode=getMode()
	message=getMessage()
	key=getKey()
	system ("d")
	print (getTranslatedMessage(mode,message,key))
	mode=getMode()
	message=getMessage()
	if mode[0]!='b':
		key=getKey()
	system ("d")
	if mode[0]!='b':
		print (getTranslatedMessage(mode,message,key))
	else:
		for key in range (1,MAX_KEY_SIZE+1):
			print (key,getTranslatedMessage("decrypt",message,key))
	print (name+",Thank you for using.")
	print()
	input ("Enter * to quit.")
except:
	print ("\a")
	input ("Enter * to quit.")
					
