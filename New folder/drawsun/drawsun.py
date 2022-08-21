import turtle

def draw_square(sam_turtle):
    for i in range (1, 5):
        sam_turtle.forward(200)
        sam_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    sun = turtle.Turtle()
    sun.shape("turtle")
    sun.color("yellow")
    sun.speed(4)
    sun.pensize(2)
    for i in range (1, 37):
        draw_square(sun)
        sun.right(10)
    window.exitonclick()
draw_art()