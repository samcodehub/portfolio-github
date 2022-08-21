import turtle
Cppsecrets = turtle.Screen()
Cppsecrets.bgcolor('black')
s = turtle.Turtle()
s.speed(11)
s.color('white')
rotate=int(180)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def Cppsecrets1(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)
Cppsecrets1(s,150,10)
t1 = turtle.Turtle()
t1.speed(11)
t1.color('orange')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t1,130,10)
t2= turtle.Turtle()
t2.speed(11)
t2.color('blue')
rotate=int(80)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t2,100,10)


turtle.done()