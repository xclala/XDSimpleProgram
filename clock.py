from turtle import Pen,done,screensize
from random import choice
t=Pen()
colors=choice(["orange","yellow","green","cyan"])
screensize(canvwidth=1, canvheight=1, bg=colors)
try:
	t.hideturtle()
	from time import asctime,localtime,time
	while True:
		localtimes=asctime(localtime(time()))
		t.write (localtimes,font=10)
		t.undo()
	done()
except:
	pass
