import Gameplay
import winsound
import turtle


screen = turtle.Screen()

def Set_Back_Ground():
    screen.setup(900,518)
    screen.bgpic("Scrap\\intro.gif")

def about():
    x = turtle.Screen()
    x.bgcolor("white")
    x.setup(410,468)
    x.bgpic("Scrap\\About.gif")
    y = turtle.Turtle()
    y.speed(0)
    y.penup()
    y.setpos(-200,-200)
    y.write("<<BACK",align="left",font=("Arial",20,"normal"))
    x.onclick(back)

def back(x,y):
    if(-200 < x < -100):
        screen.clearscreen()
        screen.onclick(None)
        Menu()

def Menu():
    winsound.PlaySound("Music\\Menu.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    Set_Back_Ground()
    menu = turtle.Turtle()
    menu.speed(0)
    menu.penup()
    menu.setpos(0,-200)
    menu.write("Play",align="center",font =("Arial",20,"normal"))
    menu.setpos(-225, -200)
    menu.write("About", align ="center",font=("Arial",20,"normal"))
    menu.setpos(225, -200)
    menu.write("Quit", align="center", font=("Arial", 20, "normal"))
    menu.ht()
    menu.setpos(0, -80)
    screen.onscreenclick(onclick_event)

def onclick_event(x, y):
    if (-250 < y < 250):
        if (-30 < x < 30):
            screen.clearscreen()
            screen.onclick(None)
            Gameplay.race()
        if (-300 < x < -100):
            screen.clearscreen()
            screen.onclick(None)
            about()

        if (150 < x < 300):
            screen.clearscreen()
            screen.onclick(None)
            quit()

