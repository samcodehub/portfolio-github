from turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(120):
    color('sienna')
    circle(i)
    color('chocolate')
    circle(i*0.8)
    right(3)
    forward(3)
done()
