import time
import turtle

t = turtle.Screen()
t.bgcolor("white")
t.setup(width=600, height=600)
t.tracer(0)
t.title('Analog Clock')

# create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(20)
pen.pensize(15)

def draw_clock(h, m, s, pen):
    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("darkgoldenrod")
    pen.pendown()
    pen.circle(210)
    
    # Draw the lines for the hours
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    
    # Draw the hour hands
    pen.penup()
    pen.goto(0, 0)
    pen.color("black")
    pen.setheading(90)
    angle = (h/12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    
    # Draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)
    
    # Draw the second hands
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (s/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)
    
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    draw_clock(h, m, s, pen)
    t.update()
    pen.clear()
    time.sleep(1)

t.mainloop()