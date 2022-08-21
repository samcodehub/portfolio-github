'''1.”pip install pygame”

2.”py -m pip install -U pygame -user”

3.”py -m pip install pygame”'''

import pygame, sys
pygame.init() #initialize the pygame
from pygame.locals import * # importing all madule from pygame
import random
import math
import time
screen = pygame.display.set_mode((798,600))

# initialize pygame mixer
pygame.mixer.init() 

# changing title of the game window
pygame.display.set_caption('Car Race Game')

# changing the logo  of the game
logo = pygame.Image.load('logo.jpeg')
pygame.display.set_icon(logo)

# making intro to the game
IntroFont = pygame.font.Font("freesansbold.ttf", 38)
def introImg(x,y):
    intro = pygame.image.Image.load("intro.png")
    screen.blit(intro,(x,y))
    
def instructionIMG(x,y):
    instruct = pygame.image.load("instruction.png")
    run = True
    while run:
        screen.blit(instruct,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
def aboutIMG(x,y):
    aboutimg = pygame.image.load("About.png")
    run = True
    while run:
        screen.blit(aboutimg,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
def play(x,y):
    playtext = IntroFont.render("PLAY",True,(255,0,0))
    screen.blit(playtext,(x,y))
def ABOUT(x,y):
    abouttext = IntroFont.render("ABOUT",True,(255,0,0))
    screen.blit(abouttext,(x,y))
def Instruction(x,y):
    instructiontext = IntroFont.render("INSTRUCTION",True,(255,0,0))
    screen.blit(instructiontext,(x,y))
    
def introscreen():
    run = True
    pygame.mixer.music.load('startingmusic.mp3')
    pygame.mixer.music.play()
    while run:
        screen.fill((0,0,0))
        introImg(0,0)
        play(100,450)
        Instruction(615,450)
        
# getting mouse cursor coordinates
x,y = pygame.mouse.get_pos()

# storing rectangle coordinate (x,y, length) by making variables
button1 = pygame.Rect(60,440,175,50)
button2 = pygame.Rect(265,440,300,50)
button3 = pygame.Rect(600,440,165,50)

# drawing rectangle with stored coordinates of rectangles
# pygame.draw.Rect takes these arguments (surface, color, coordinates, border)
pygame.draw.rect(screen,(255,255,255), button1,6)
pygame.draw.rect(screen,(265,255,255), button2,6)
pygame.draw.rect(screen,(255,255,255), button3,6)

# if our cursor is on button1 which is play button
if button1.collidepoint(x,y):
    # changing from inactive to active by changing the color from white to red 
    pygame.draw.rect(screen, (155,0,0), button1,6)
    # if we click on the play button 
    if click:
        countdown() # calling countdown function to start our Game
# if our cursor is on button2 which is instruction button
if button2.collidepoint(x,y):
    # changing from inactive to active by changing the color from white to red
    pygame.draw.rect(screen, (155,0,0), button2,6)
    # if we click on the instruction button
    if click:
        instructionIMG(0,0) # displaying our instruction Image
    
        
    # if our cursor is on button3 which is about button 
if button3.collidepoint(x,y):
    # changing from inactive to active by changing the color from white to red
    pygame.draw.rect(screen,(155,0,0),button3,6)
    # if we click on the about button
    if click:
        aboutIMG(0,0) # displaying our about image
        
# checking from mouse click event
click = False
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            click = True
pygame.display.update()

# countdown
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBackground = pygame.image.load('bg.png')
    three = font2.render('3', True, (187,30,16))
    two = font2.render('2', True,(255,255,0))
    one = font2.render('1', True,(51,165,50))
    go = font2.render('GO!!!',True,(0,255,0))
        
# display blank background
screen.blit(countdownBacground,(0,0))
pygame.display.update()

# display three (3)
screen.blit(three,(350,250))
pygame.display.update()
time.sleep(1)

# display blank background
screen.blit(countdownBackground,(0,0))
pygame.display.update()
time.sleep(1)

# display two (2)
screen.blit(two,(350,250))
pygame.display.update()
time.sleep(1)

# display blank background
screen.blit(countdownBackground,(0,0))
pygame.display.update()
time.sleep(1)

# display one (1)
screen.blit(one,(350,250))
pygame.display.update()
time.sleep(1)

# display blank background
screen.blit(countdownBackground,(0,0))
pygame.display.update()
time.sleep(1)

# display go!!!
screen.blit(go,(300,250))
pygame.display.update()
time.sleep(1)
gameloop() # calling the gameloop so that the game start
pygame.display.update()

# defining pur gameloop
def gameloop():
    # music 
    pygame.mixer.music.load('BackgroundMusic.mp3')
    pygame.mixer.music.play()

# sound effects for collision
crash_sound = pygame.mixer.sound('car_crash.wav')

# scoring part 
score_value = 0
font1 = pygame.font.Font("freesansbold.ttf", 25)

def show_score(x,y):
    score = font1.render("SCORE:" + str(highscore),True, (255,0,0))
    screen.blit(score,(x,y))
    
# highscore part
with open ("highscore.txt","r") as f:
    highscore = f.read()

def show_highscore(x,y):
    Hiscore_text = font1.render("HIGHSCORE:" + str(highscore),True,(255,0,0))
    screen.blit(Hiscore_text,(x,y))
    pygame.display.update()
    
# create our game  over function
def gameover():
    gameoverImg = pygame.image.load("gameover.png")
    run = True
    while run:
        screen.blit(gameoverImg,(0,0))
        time.sleep(0.5)
        show_score(330,400)
        time.sleep(0.5)
        show_highscore(330,450)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    countdown()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# setting our player 
maincar = pygame.image.load('car.png')
maincarX = 350
maincarY = 495
maincarX_change = 0
maincarY_change = 0

# other cars  
car1 = pygame.image.load('car1.png')
car1X = random.randint(178,490)
car1Y = 100 
car1Ychange = 10 
car2 = pygame.image.load('car2.png')
car2X = random.randint(178,490)
car2Y = 100 
car2Ychange = 10 

car3 = pygame.image.load('car3.png')
car3X = random.randint(178,490)
car3Y = 100 
car3Ychange = 10 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
# checking if anykey has been pressed
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                maincarX_change += 5  
                
            if event.key == pygame.K_LEFT:
                maincarX_change -= 5
                
            if event.key == pygame.K_UP:
                maincarY_change -= 5
            
            if event.key == pygame.K_DOWN:
                maincarY_change += 5
                
        # cheking if key has been lifted up 
        if event.key == pygame.KEYUP:
            if event.type == pygame.K_RIGHT:
                maincarX_change = 0
            if event.type == pygame.K_LEFT:
                maincarX_change = 0
                
            if event.key == pygame.K_UP:
                maincarY_change = 0
            if event.key == pygame.K_DOWN:
                maincarY_change = 0
                
# setting boundary for our main car  
    if maincarX < 178:
        maincarX = 178
    if maincarX > 490:  
        maincarX = 490
    
    if maincarY < 0:
        maincarY = 0
    if maincarY > 495: 
        maincarY = 495
        
# changing color with rgb values
screen.fill((0,0,0))

# displaing the background image
screen.blit(bg,(0,0,))

# displaying our main car
screen.blit(car1,(car1X,car1Y))
screen.blit(car2,(car2X,car2Y))
screen.blit(car3,(car3X,car3Y))

# calling our show score function
show_score(570,280)

# calling our show highscore function
show_highscore(0,0)

# updating the values
maincarX += maincarX_change
maincarY += maincarY_change

# movement of the enemies
car1Y += car1Ychange
car2Y += car2Ychange
car3Y += car3Ychange

# moving enemis infinitely
if car1Y > 670:
    car1Y = -100
    car1X = random.randint(178,490)
    score_value += 1 
    
if car2Y > 670:
    car2Y = -150
    car2X = random.randint(178,490)
    score_value += 1
    
if car3Y > 670:
    car3Y = -200
    car3X = random.randint(178,490)
    score_value += 1
    
# checking if highscore has been created
if score_value > int(highscore):
    highscore = score_value
    
# detecting collision between the cars 
def iscollision(car1X,car1Y,maincarX,maincarY):
    distance = math.sqrt(math.pow(car1X-maincarX,2) + math.pow(car1Y-maincarY,2))
    
# checking if distance is smaller than 50 after than collision will occur
    if distance < 50:
        return True
    else:
        return False

# getting distance between our main car and car2  
def iscollision(car2X,car2Y,maincarX,maincarY):
    distance = math.sqrt(math.pow(car2X-maincarX,2) + math.pow(car2Y - maincarY,2))
    
    # checking if distance is smaller than 50 after than collision will occur
    if distance < 50:
        return True
    else:
        return False

# getting distance between our main car and car3  
def iscollision(car3X,car3Y,maincarX,maincarY):
    distance = math.sqrt(math.pow(car3X-maincarX,2) + math.pow(car3Y-maincarY))
    if distance < 50:
        return True
    else:
        return False
    
# giving collision a variable 
# collision between maincar and car1  
coll1 = iscollision(car1X,car1Y,maincarX,maincarY)
coll2 = iscollision(car2X,car2Y,maincarX,maincarY)
coll3 = iscollision(car3X,car3Y,maincarX,maincarY)

# if coll occure
if coll1:
    car1Ychange = 0
    car2Ychange = 0
    car3Ychange = 0
    car1Y = 0
    car2Y = 0
    car3Y = 0
    maincarX_change = 0
    maincarY_change = 0
    pygame.mixer.music.stop()
    crash_sound.play()
    
# calling our game over function   
    time.sleep(1)
    gameover()
    
#if coll2 occure
if coll2:
    car1Ychange = 0
    car2Ychange = 0
    car3Ychange = 0
    car1Y = 0
    car2Y = 0
    car3Y = 0
    maincarX_change = 0
    maincarY_change = 0
    pygame.mixer.music.stop()
    crash_sound.play()
    time.sleep(1)
    gameover()
    
# if coll3 occure
if coll3:
    car1Ychange = 0
    car2Ychange = 0
    car3Ychange = 0
    car1Y = 0
    car2Y = 0
    car3Y = 0
    maincarX_change = 0
    maincarY_change = 0
    pygame.mixer.music.stop()
    crash_sound.play()
    time.sleep(1)
    gameover()
    
if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0:
    pass

# writing to our highscore.txt file
with open("car game\highscore.txt", "w") as f:
    f.write(str(highscore))
    
pygame.display.update()
introscreen()

        
            
    



    