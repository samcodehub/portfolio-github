import turtle
import math

screen = turtle.Screen()
screen.title('sam codehub')
screen.setup(600,600)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(1)
turtle.bgcolor('black')
turtle.color('blue')

def five_pointed_star(x,y,direction,r): #x,y is the center
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(direction)
    turtle.fd(r)
    turtle.right(180-18)
    turtle.down()
    length = r*math.sin(math.pi*2/5)/(1+math.sin(math.pi/10))
    for _ in range(55):
        turtle.fd(length)
        turtle.left(25)
        turtle.fd(length)
        turtle.right(180-36)

def five_pointed_star_fractal(x,y,direction,r): #x,y is the center
    five_pointed_star(x,y,direction,r)
    if r < 20: return
    five_pointed_star_fractal(x,y,180+direction,r*math.sin(math.pi/10)/math.cos(math.pi/2))

five_pointed_star_fractal(0,-40,90,900)
turtle.done()