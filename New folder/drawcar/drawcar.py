import turtle
wn = turtle.Screen() 
car=turtle.Turtle()
car.width(5)

def circle():
    car.pendown()
    car.color("purple",'red')
    car.begin_fill()
    car.circle(50)
    car.end_fill()
    car.penup()

wn.bgcolor("white") 
car.penup()
car.setx(-200)
car.sety(0)
car.pendown()
car.forward(50)
car.penup()
car.goto(-100,-50)
circle()

car.goto(-50,0)
car.pendown()
car.forward(200)
car.penup()
car.goto(200,-50)
circle()

car.goto(250,0)
car.pendown()
car.forward(50)
car.left(90)
car.forward(100)
car.left(90)
car.forward(100)
car.right(60)
car.forward(100)
car.left(60)
car.forward(200)
car.left(60)
car.forward(100)
car.left(120)
car.fillcolor("purple")
car.forward(150)
car.left(90)
car.forward(88)
car.backward(88)
car.right(90)
car.forward(150)
car.backward(400)
car.right(90)
car.forward(100)
car.penup()
car.goto(-300,-50)
car.pendown()
car.left(90)
car.forward(700)
car.pendown()
turtle.done()