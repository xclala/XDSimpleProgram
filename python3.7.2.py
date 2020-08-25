try:
	from os import system
	system("a")
	with open('写代码.txt') as file_object:
		contents = file_object.read()
		contents=exec(contents)
		print(contents)
		system("b")
		input("执行完毕，请按任意键退出...")
except Exception as e:
	print("Error or Warning:"+e)
	input("请按任意键退出...")
