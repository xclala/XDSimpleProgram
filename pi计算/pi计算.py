try:
	from time import perf_counter
	from gc import collect
	def Bar(i):
		N=10**level
		a=int((i/N)*50)
		b=50-a
		Y,N='*'*a,'.'*b
		print("\r计算中:{:3.0f}%[{}->{}]{:.2f}s".format(2*a,Y,N,perf_counter()),end='')
	while True:
		level=eval(input("\n计算pi精确到小数点后几位数？"))
		l=int(level)
		if l==1:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.3")
		elif l==2:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.12")
		elif l==3:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.14")
		elif l==4:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.1414")
		elif l==5:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.14157")
		elif l==6:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.141591")
		elif l==7:
			print("\n计算开始")
			print("\n计算完成")
			print("\npi的计算值为3.1415925")
		else:
			print('\n{:=^70}'.format('计算开始'))
			a,b,pi,tmp,i=1,1,0,1,0
			perf_counter()
			while (abs(tmp)>=10**-level):
				pi += tmp
				b +=2
				a=-a
				tmp=a/b
				i+=2
				Bar(i)
			print("\n{:=^70}".format('计算完成'))
			print("\npi的计算值为：{}".format(round(pi*4,level)))
			del a,level,tmp,i,pi,b
			collect()
except Exception as e:
	print(e)
