import turtle as tt

# set the background color
tt.bgcolor("black")

# set the pen Size
tt.pensize(2)  

# set the pen speed   
tt.speed(11)
# iterate 8 times 
for i in range(8):
    #color combination
    for color in('purple','magenta','blue','cyan','green','white','brown'):
        tt.color(color)
        # draw a circl of choosen size
        tt.circle(100)
        # move 10 px left to draw other circles
        tt.left(10)
    #hide the cursor
    tt.hideturtle()
tt.done()