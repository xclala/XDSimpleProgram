try:
	name=input("您怎么称呼？")
	print ("你好，%s！"%(name))
	dog_age=int(input("%s，你家狗狗几岁？"%(name)))
	if dog_age<=0:
		print("\a%s，你在逗我吧！"%(name))
		input("%s，请按任意键退出。"%(name))
		del name,dog_age
	else:
		person_age=22+(dog_age-2)*5
		print(name+"，对应人类年龄",person_age,"岁。")
		input("%s，请按任意键退出。"%(name))
		del name,person_age,dog_age
except:
	pass