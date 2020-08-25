try:
	name=input ("您怎么称呼？")
	print ("你好，"+name+"!")
	print (name+"，欢迎抽奖！祝您好运！")
	input (name+"，开始抽奖?")
	while True: 
		from random import randint
		num1=input(name+"，请您输入最多25位抽奖号码。")
		input (name+"，你准备好了吗？")
		print (name+"，正在抽奖中。。。")
		random_number1=str(randint(0,9999999999999999999999999))
		random_number2=str(randint(0,9999999999999999999999999))
		random_number3=str(randint(0,9999999999999999999999999))
		if num1==random_number1:
			if num1==random_number2:
				if num1==random_number3:
					print (name+"，恭喜你，中一等奖了！")
					c=input (name+"，您还要继续抽奖吗？（是/不是）")
					if c=='不是':
						break
				else:
					print (name+"，恭喜你，中二等奖了！")
					d=input (name+"，您还要继续抽奖吗？（是/不是）")
					if d=='不是':
						break
			else:
				print (name+"，恭喜你，中三等奖了！")
				e=input (name+"，您还要继续抽奖吗？（是/不是）")
				if e=='不是':
					break
		else:
			print (name+"，对不起，您没中奖。")
			f=input (name+"，您还要继续抽奖吗？（是/不是）")
			if f=='不是':
				break
	del name,c,d,e,f,num1,random_number1,random_number2,random_number3
except:
	pass