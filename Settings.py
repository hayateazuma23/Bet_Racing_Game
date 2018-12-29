import math
import random
import turtle
from Gameplay import *


def Setting_bg():
    koi = turtle.Screen()
    koi.setup(900, 500)
    koi.bgpic("Scrap\\Setting.gif")
    cha = turtle.Turtle()
    cha.penup()
    cha.setpos(0, 200)
    cha.write("Setting", align="center", font=("Arial", 30, "normal"))


def Generate_Speed(choice):
    if (choice == 1):
        filename = "Characters\\Animal\\Speed"
    elif (choice == 2):
        filename = "Characters\\Marvel\\Speed"
    elif (choice == 3):
        filename = "Characters\\Monsters\\Speed"
    elif (choice == 4):
        filename = "Characters\\Pokemon\\Speed"
    elif (choice == 5):
        filename = "Characters\\SpaceShip\\Speed"
    else:
        print("Can't find file !!")
    f = open(filename, "r")
    f.seek(15, 0)
    max = f.readline()
    f.seek(33, 0)
    min = f.readline()
    max = max.split("\n", )
    max = int(max[0])
    min = min.split("\n", )
    min = int(min[0])
    Total = round(((max - min + 1) / (75 / 100)))
    Total_standing_backward = Total - (max - min + 1)
    Standing = math.floor(Total_standing_backward * (20 / 100) / (25 / 100))
    Backward = Total_standing_backward - Standing
    list_speed = []
    for step in range(min, max + 1):
        list_speed.append(step)
    for step in range(1, Standing + 1):
        list_speed.append(0)
    for step in range(1, Backward + 1):
        list_speed.append(0 - step)
    return list_speed[random.randint(0, Total - 1)]


def Win_Lose_Condition(Bet, ID):
    if (Bet == ID + 1):
        return 1
    else:
        return -1


def End_Match_Condition(list_characters, FinishLine):
    if (list_characters[0].character.xcor() < FinishLine or
            list_characters[1].character.xcor() < FinishLine or
            list_characters[2].character.xcor() < FinishLine or
            list_characters[3].character.xcor() < FinishLine or
            list_characters[4].character.xcor() < FinishLine):
        return 1
    else:
        return 0


def Check_Who_First(list_time):
    list_ID_rank = [0, 1, 2, 3, 4]
    c = list(zip(list_time, list_ID_rank))
    c.sort()
    list_time, list_ID_rank = zip(*c)
    return list_ID_rank
