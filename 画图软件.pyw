from tkinter import *
from turtle import *
t = Turtle()
root = Tk()
root.withdraw()
t.hideturtle()
t.speed(0)
a = Entry()
a.pack(side=LEFT, expand=True, fill=X)


def fw():
    t.forward(int(a.get()))


def lf():
    t.left(int(a.get()))


def rh():
    t.right(int(a.get()))


def cc():
    t.circle(int(a.get()))


def pencr():
    t.pencolor(a.get())


def pensz():
    t.pensize(int(a.get()))


def writ():
    t.write(a.get())


def ud():
    t.undo()


def rst():
    t.reset()


def triangle():
    t.circle(int(a.get()), steps=3)


def square():
    t.circle(int(a.get()), steps=4)


def five():
    t.circle(int(a.get()), steps=5)


def six():
    t.circle(int(a.get()), steps=6)


Button(text='前进', command=fw).pack(side=RIGHT)
Button(text='向左', command=lf).pack(side=RIGHT)
Button(text='向右', command=rh).pack(side=RIGHT)
Button(text='圆', command=cc).pack(side=RIGHT)
Button(text='颜色', command=pencr).pack(side=RIGHT)
Button(text='粗细', command=pensz).pack(side=RIGHT)
Button(text='单步撤回', command=ud).pack(side=RIGHT)
Button(text='清空', command=rst).pack(side=RIGHT)
Button(text='三角形', command=triangle).pack(side=RIGHT)
Button(text='正方形', command=square).pack(side=RIGHT)
Button(text='五边形', command=five).pack(side=RIGHT)
Button(text='六边形', command=six).pack(side=RIGHT)
mainloop()
