from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'navy')
    back(100)
    right(120)
    forward(100)
    dot(120, 'maroon')
    back(100)
    right(120)
    forward(100)
    dot(120, 'gold')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10
    
title("Pinwheel")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'Right')
listen()
animate()
done()