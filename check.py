def draw (python , c):
    if python >0:
        turtle.forward(python)
        turtle.right(c)
        draw(python-2,c)
import turtle
turtle.shape('turtle')
turtle.bgcolor('chartreuse')
turtle.reset()
turtle.pen(speed =1)
turtle.delay(0)
length =450
turn_by =121
turtle.penup()
turtle.setpos(-length/2,length/2)
turtle.pendown()
draw(length,turn_by)
turtle.hideturtle()
turtle.done()