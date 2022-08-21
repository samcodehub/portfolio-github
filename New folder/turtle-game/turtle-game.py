import turtle   
import random

player_1 = turtle.Turtle()
player_1.color('green')
player_1.shape("turtle")
player_1.penup()
player_1.goto(-200, 100)
player_2 = player_1.clone()
player_2.color('yellow')
player_2.penup()
player_2.goto(-200, -100)

player_1.goto(200, 60)
player_1.pendown()
player_1.circle(40) 
player_1.penup()
player_1.goto(-200, 100)
player_2.goto(200, -140)
player_2.pendown()
player_2.circle(40)
player_2.penup()
player_2.goto(-200, -100)

die = [1,2,3,4,5,6]

while(1):
    if player_1.pos() >= (200, 100):
        print("Player1 win!")
        break
    elif player_2.pos() >= (200, -100):
        print("Player2 win!")
        break
    else:
        player_1_turn = input("press 'Enter' to roll die:")
        die_outcome = random.choice(die) 
        print("the result of the roll die is: ")
        print(die_outcome)
        print("the number of the steps will be: ")
        print(20*die_outcome)
        player_1.fd(20*die_outcome)
        player_2_turn = input("press 'Enter' to roll die: ")
        die_outcome = random.choice(die)
        print("the result of the roll die is: ")

        print(die_outcome)
        print("the number of the steps will be: ")
        print(20*die_outcome)
        player_2.fd(20*die_outcome)        