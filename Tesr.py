'''import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("song2.wav")
pygame.mixer.music.play(-1)
while pygame.mixer.music.get_busy():
   time.sleep(1)'''


import turtle


def a():
    screen = turtle.Screen()
    screen.clearscreen()
    screen.bgcolor("black")
    announce = turtle.Turtle()
    announce.ht()
    screen.register_shape("Scrap\\Win.gif")
    screen.register_shape("Scrap\\Lose.gif")
    screen.register_shape("Scrap\\Replay.gif")
    announce.penup()
    announce.goto(0, 0)
    announce.showturtle()
    announce.shape("Scrap\\Win.gif")

    replay = turtle.Turtle()
    replay.penup()
    replay.goto(-100, -100)
    replay.shape("Scrap\\Replay.gif")
    replay.onclick(b)


def b(x,y):
    e.clearscreen()
    e.onclick(None)
    a()

w = turtle.Turtle()
e = turtle.Screen()
w.onclick(b)
turtle.done()

