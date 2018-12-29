import turtle
import Gameplay
import RaceTrack
import Menu
import winsound

main_screen = turtle.Screen()


def Annoucement(condition, list_ID_rank, list_names, list_time):
    screen = turtle.Screen()
    screen.clearscreen()
    screen.bgcolor("black")
    announce = turtle.Turtle()
    announce.ht()
    screen.register_shape("Scrap\\Win.gif")
    screen.register_shape("Scrap\\Lose.gif")
    announce.penup()
    announce.goto(0, 100)
    announce.showturtle()
    if (condition == 1):
        winsound.PlaySound("Music\\Win.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        announce.shape("Scrap\\Win.gif")
    else:
        winsound.PlaySound("Music\\Lose.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        announce.shape("Scrap\\Lose.gif")

    RaceTrack.Ranking(list_ID_rank, list_names, list_time)
    t = turtle.Turtle()
    t.penup()
    t.pencolor("white")
    t.speed(0)
    t.goto(-200,-100)
    t.write("<<Replay",align="center",font=("Arial",20,"normal"))
    t.goto (200,-100)
    t.write(">>Back to Menu", align="center", font=("Arial", 20, "normal"))
    t.ht()
    screen.onclick(onclick_replay)



def onclick_replay(x,y):
    if (-150< y < 0):
        if (-150 < x < 100):
            main_screen.clearscreen()
            main_screen.onclick(None)
            Gameplay.race()
        if (150 < x < 200):
            main_screen.clearscreen()
            main_screen.onclick(None)
            Menu.Menu()

