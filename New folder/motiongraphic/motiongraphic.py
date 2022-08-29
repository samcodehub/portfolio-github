import turtle
import colorsys
import random
import math

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("motion graphic")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

screen.bgcolor('black')
firefly = turtle.Turtle() # turtle for drawing the lighting dot
firefly.hideturtle()
firefly.up()

# Constants
H_YELLOWGREEN = 0.22 # constant: hue value of yellow green color.
V_DARK = 0.1 # constant: brightness value of initial dark state
V_BRIGHT = 1 # constant: brightness value of the brightest state
FPS = 30 # constant: refresh about 30 times per second
TIMER_VALUE = 1000//FPS # the timer value in milliseconds for timer events
CYCLE = 5 # costant: 5 second cycle for firefly to light up
LIGHTUP_TIME = 1 # constant: 1 second light up and dim
SPEED = 100 # 100 units per second
CLOSE_ENOUGH = 16 # if distance squared to target is less than 16, then it is close enough.

# Variables
v = V_DARK # initial brightness state
t = 0 # current time
current_xpos = 0 # current x coordinate
current_ypos = 0 # current y coordinate
target_xpos = random.randint(-300,300) # target x coordinate, random location
target_ypos = random.randint(-300,300) # target y coordinate, random location
should_draw = True # this variable is used to decide if drawing is necessary to save CPU time

def update_brightness():
    global t,v
    if t > CYCLE:
        t -= CYCLE # make sure time stays within CYCLE
    if t < CYCLE-LIGHTUP_TIME:
        v = V_DARK # dormant period
    elif t < CYCLE-LIGHTUP_TIME/2: # gradually (linearly) lighting up period
        v = V_DARK + (V_BRIGHT-V_DARK)*(t-(CYCLE-LIGHTUP_TIME))/(LIGHTUP_TIME/2)
    else: # gradually (linearly) dimming period
        v = V_BRIGHT - (V_BRIGHT-V_DARK)*(t-(CYCLE-LIGHTUP_TIME/2))/(LIGHTUP_TIME/2)

def update_position():
    global current_xpos,current_ypos,target_xpos,target_ypos
    # move towards target SPEED/FPS steps
    # figure out angle to target first
    angle_to_target = math.atan2(target_ypos-current_ypos,target_xpos-current_xpos)
    # compute changes to current position based on the angle and distance to move per 1/FPS second.
    current_xpos += SPEED/FPS*math.cos(angle_to_target)
    current_ypos += SPEED/FPS*math.sin(angle_to_target)
    #print(current_xpos,current_ypos,target_xpos,target_ypos)
    # check to see if close enough to target.
    dist_to_target_squared = (current_xpos-target_xpos)**2 + (current_ypos-target_ypos)**2
    if dist_to_target_squared < CLOSE_ENOUGH: # close enough, set new target
        target_xpos = random.randint(-300,300) # target x coordinate, random location
        target_ypos = random.randint(-300,300) # target y coordinate, random location
        

def update_states():
    global t,should_draw
    t += TIMER_VALUE/1000 # every time this function is called, time increases by this value
    update_brightness()
    update_position()
    should_draw = True
    screen.ontimer(update_states,TIMER_VALUE)

def draw():
    global v,firefly,should_draw,current_xpos,current_ypos
    if should_draw == False: # There is no change. Don't draw and return immediately
        return
    firefly.clear() # clear the current drawing
    color = colorsys.hsv_to_rgb(H_YELLOWGREEN,1,v) # use colorsys to convert HSV to RGB color
    firefly.color(color)
    firefly.goto(current_xpos,current_ypos)
    firefly.dot(200)
    should_draw = False # just finished drawing, set should_draw to False
    
screen.ontimer(update_states,TIMER_VALUE)
while True:
    draw() # draw forever
    screen.update()