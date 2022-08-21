from turtle import Turtle as Tu
from turtle import Screen
from math import pi
import time

def round_trip(tur, size):
    tur.fd(size)
    tur.bk(size)

def start(tur):
    tur.pu()
    tur.rt(90)
    tur.fd(40)
    tur.lt(90)
    tur.pd()
    
def decor(tur , size):
    tur.lt(90)
    tur.fd(100*pi/30)
    tur.rt(96)
    round_trip(tur, size)
    
def end(tur):
    tur.color("maroon")
    tur.bk(500)    
        
def center(tur, color):
    tur.reset()
    tur.speed(0)
    tur.pu()
    tur.lt(90)
    tur.fd(60)
    tur.color(color)
    tur.pd()
            
def draw_time(tu,angle, lengt):
    tu.speed(0)
    tu.rt(angle)
    tu.fd(lengt)
        
screen = Screen()
clock = Tu()

screen.bgcolor("maroon")
clock.color("black")
clock.speed(100)


start(clock)
clock.begin_fill()
clock.circle(100)
clock.end_fill()
end(clock)

clock_decor = Tu()
clock_decor.color("yellow")
clock_decor.speed(1000)

start(clock_decor)
clock_decor.lt(87)

for i in range(12):
    round_trip(clock_decor, 20)
    for j in range(5):
        decor(clock_decor, 10)
end(clock_decor)

H = Tu()
M = Tu()
S = Tu()

furst = True

while True:
    
    T = time.time()
    h = ((T/3600)%12)*360/12
    m = ((T/60)%60)*(360/60//6)*6
    s = (T%60)*(360/60//6)*6

    clockwise1 = {H:"white", M:"blue", S:"red"}
    clockwise2 = {H:(h,40), M:(m,60), S:(s,80)}

    if furst:

        for i, j in clockwise1.items():
            center(i, j)
        
        for i, j in clockwise2.items():
            draw_time(i,j[0],j[1])
        
        furst = False
    
    center(S, clockwise1[S])
    draw_time(S,clockwise2[S][0],clockwise2[S][1])
    for i in range(30):
            S.fd(0)
    if not s//6 :
    
        center(M, clockwise1[M])
        draw_time(M,clockwise2[M][0],clockwise2[M][1])
        
    if not m :
    
        center(H, clockwise1[H])
        draw_time(H,clockwise2[H][0],clockwise2[H][1])