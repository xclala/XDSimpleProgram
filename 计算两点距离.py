try:
	while True:
		from math import sqrt
		dimension=input("维度(1-4)：")
		if dimension=='1':
			x1_one=int(input("x1="))
			x2_one=int(input("x2="))
			distance_one=abs(x1_one-x2_one)
			del x1_one,x2_one
			print("距离",distance_one)
			del distance_one
		elif dimension=='2':
			x1_two=int(input("x1="))
			x2_two=int(input("x2="))
			y1_two=int(input("y1="))
			y2_two=int(input("y2="))
			distance_two=abs(sqrt((x1_two-x2_two)**2+(y1_two-y2_two)**2))
			del x1_two,x2_two,y1_two,y2_two
			print("距离",distance_two)
			del distance_two
		elif dimension=='3':
			x1_three=int(input("x1="))
			x2_three=int(input("x2="))
			y1_three=int(input("y1="))
			y2_three=int(input("y2="))
			z1_three=int(input("z1="))
			z2_three=int(input("z2="))
			from math import sqrt
			distance_three=abs(sqrt((x1_three-x2_three)**2+(y1_three-y2_three)**2+(z1_three-z2_three)**2))
			del x1_three,x2_three,y1_three,y2_three,z1_three,z2_three
			print("距离",distance_three)
			del distance_three
		elif dimension=='4':
			x1=int(input("x1="))
			x2=int(input("x2="))
			y1=int(input("y1="))
			y2=int(input("y2="))
			z1=int(input("z1="))
			z2=int(input("z2="))
			w1=int(input("w1="))
			w2=int(input("w2="))
			from math import sqrt
			distance=abs(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2+(w1-w2)**2))
			del x1,x2,y1,y2,z1,z2,w1,w2
			print("距离",distance)
			del distance
		else:
			input("输入错误！请按任意键退出。\a")
except KeyboardInterrupt:
	pass
except:
	input("输入错误！请按任意键退出。\a")
