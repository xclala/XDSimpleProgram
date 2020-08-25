while True:
	try:
		from calendar import month,isleap
		from os import system
		system("color f0")
		year=int(input("年份："))
		mon=input("月份：")
		if isleap(year)==True:
			if mon=='':
				for i in range(1,13):
					print()
					print(year,"年是闰年")
					print(month(year,i))
			else:
				mon=int(mon)
				print()
				print(year,"年是闰年")
				print(month(year,mon))
		else:
			if mon=='':
				for i in range(1,13):
					print()
					print(year,"年是平年")
					print(month(year,i))
			else:
				mon=int(mon)
				print()
				print(year,"年是平年")
				print(month(year,mon))
	except (ValueError,EOFError,IndexError):
		print("输入错误！\a")
	except KeyboardInterrupt:
		from os import _exit
		_exit(0)
	except:
		pass
