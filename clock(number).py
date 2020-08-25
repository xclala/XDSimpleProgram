def clock_number():
	from turtle import Pen,done,screensize
	from random import choice
	t=Pen()
	colors=choice(["orange","yellow","green","cyan","gold","pink","tomato"])
	screensize(canvwidth=1, canvheight=1, bg=colors)
	del colors
	try:
		t.hideturtle()
		from time import asctime,localtime,time
		while True:
			localtimes=asctime(localtime(time()))
			t.write (localtimes,font=10)
			del localtimes
			t.undo()
		done()
		del t
		except:
			pass
from dis import dis
dis(clock_number)
input()