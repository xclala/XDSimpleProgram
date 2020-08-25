try:
	from os import system
	import pyttsx3
	engine=pyttsx3.init()
	engine.say("您要使用“经典抽奖”还是“号码抽奖”？")
	engine.runAndWait()
	program_input=input("您要使用“经典抽奖”还是“号码抽奖”？")
	if program_input=='经典抽奖' and '经典':
		system("经典抽奖")
	elif program_input=='号码抽奖' and '号码':
		system("号码抽奖")
except:
	pass