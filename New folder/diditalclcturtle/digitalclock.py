import time
import datetime as dt  
import turtle

# create a turtle to display time
t = turtle.Turtle()
t.color("#f6fa05")
t.goto(-130, 0)

# create a turtle to create rectangle box
t1 = turtle.Turtle()
# create screen 
s = turtle.Screen()

# set background color of the screen
s.bgcolor("#000917")

# obtain corrent hour,min,sec 
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(10)
t1.color("#05fad5")
t1.penup()
# set the position of the turtle
t1.goto(-145,0)
t1.pendown()

# create rectangle box   
for i in range(2):
    t1.forward(300)
    t1.left(90)
    t1.forward(80)
    t1.left(90)
    
# hide the turtle
t1.hideturtle()
while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2), font=("Arial Narrow", 50,"bold"))
    
    time.sleep(1)
    sec+=1
    if sec == 60:
        sec=0 
        min+=1
    if min == 60:
        min = 0
        hr+=1
    if hr == 13:
        hr = 1


