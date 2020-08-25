try:
	p=input ("您怎么称呼？")
	print ("你好，"+p+"!")
	print("%s，欢迎抽奖，祝您好运！"%(p))
	while True:
		input ("%s，开始抽奖?"%(p)) 
		from random import randint
		b=randint (1,1000000)
		a=randint(0,b)
		if a==0:
			print (p+"，恭喜你中奖了！")
			asd=input("%s，您还要继续抽奖吗(是/不是)"%(p))
			if asd=='不是':
				break
		else:
			print (p+"，对不起您未中奖。")
			asf=input("%s，您还要继续抽奖吗(是/不是)"%(p))
			if asf=='不是':
				break
	del a,b,p
except:
	pass