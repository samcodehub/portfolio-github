import turtle

screen = turtle.getscreen()
v = turtle.Turtle()
screen.title( "Spiral My Name")
screen.bgcolor("Black")
colors = ("red", "yellow", "blue", "green")
your_name = turtle.textinput("Enter your name", "What is your name?")
for r in range(100):
    v.color(colors[r%4])
    v.penup()
    v.fd(r*4)
    v.pendown()
    v.write(your_name, font = ("Arial", int( (r + 4) / 4), "bold" ))
    v.lt(92)
turtle.done()    