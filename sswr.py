try:
	name=input ("您怎么称呼？")
	print ("你好，"+name+"。")
	while True:
		number=float(input (name+",您需要四舍五入哪个数？"))
		number=round(number)
		print ("结果是：",number,"。")
except:
	print ("\a")
	input ("请按任意键继续。")