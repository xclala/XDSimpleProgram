try:
	a=input ("您怎么称呼？")
	print ("你好，"+a+"！")
	b=round(int(input(a+"，一共有几个头？")))
	c=round(int(input(a+"，一共有几条腿？")))
	d=b*4-c
	if d%2==0:
	    d=d//2
	    chick=b-d
	    if d<0:
		    print (a+"，本情况不存在。")
		    input (a+"，请按任意键继续。")
	    else:
		    if chick<0:
			    print (a+"，本情况不存在。")
			    input (a+"，请按任意键继续。")
		    else:
			    rabbit=str (d)
			    chick=str (chick)
			    print (a+"，鸡有"+rabbit+"只，兔有"+chick+"只。")
			    input (a+"，请按任意键继续。")
	else:
		print (a+"，本情况不存在。")
		input (a+"，请按任意键继续。")
	del a,b,c,d,chick,rabbit
except:
	print("\a")