import turtle
import random


screen = turtle.Screen()

def Set_Back_Ground():
    background = turtle.Screen()
    background.clearscreen()
    background.setup(1500,700)
    x = random.randint(1,5)
    if (x == 5):
        background.bgpic("Scrap\\background2.gif")
    if (x == 4):
        background.bgpic("Scrap\\background3.gif")
    if (x == 2):
        background.bgpic("Scrap\\background1.gif")
    if (x == 3):
        background.bgpic("Scrap\\grass.gif")
    elif (x == 1):
        background.bgpic("Scrap\\space.gif")
    background.bgcolor("black")

def Draw_RaceTrack(length, width):
    Set_Back_Ground()
    v = turtle.Turtle()
    v.pencolor("white")
    v.pensize(5)
    x = -(length / 2) + 50  # Toa độ bắt
    y = (width / 2) - 20    # đầu đường đua
    v.speed(0)
    v.penup()
    v.goto(x, y + 20)
    for step in range(15):
        v.write(step, align='center')
        v.forward(length / 15)
    v.goto(x, y)
    for step in range(6):
        v.pendown()
        v.forward((length / 15) * 14)
        v.backward((length / 15) * 14)
        v.right(90)
        v.penup()
        v.forward((width / 5))
        v.pendown()
        v.left(90)
    Draw_Finish_Line(length, width, v)
    return v.xcor()

def Draw_Finish_Line(length, width, v):
    v.penup()
    v.left(90)
    v.forward(width / 5)
    v.right(90)
    v.forward((length / 15) * 14)
    v.left(90)
    v.pendown()
    v.pensize(10)
    v.pencolor("red")
    v.forward(width)
    v.hideturtle()
    return v.xcor()

def Arrange_Characters(list_characters, length_track, width_track, list_shapes, list_rank):
    x = -(length_track / 2) + 50  # Destination
    y = (width_track / 2) - 20  # of the race track

    for ID in range(0, 5):
        rua = list_characters[ID].character
        rua.shape(list_shapes[ID][4])
        rua.speed(100)
        rua.penup()
        rua.goto(x - 44, y - (width_track / 5) *list_rank[ID] - (width_track / 10))  # Start line
        rua.pendown()
        for step in range(4):
            list_characters[ID].character.shape(list_shapes[ID][5])
            list_characters[ID].character.shape(list_shapes[ID][4])

def display_Name(list_names, list_place, Player_Bet):
    turName = turtle.Turtle()
    turName.speed(0)
    turName.penup()
    turName.goto(-690, 340)
    turName.pendown()
    turName.pensize(3)
    turName.forward(300)
    turName.right(90)
    turName.forward(120)
    turName.right(90)
    turName.forward(300)
    turName.right(90)
    turName.forward(120)

    for step in range(5):
        turName.penup()
        turName.goto(-670, 290 - 20 * step)
        turName.pencolor("white")

        if step == 0:
            turName.write("1st place: %s" % (list_names[list_place[step]]), font=("Arial", 16, "normal"))
        elif step == 1:
            turName.write("2nd place: %s" % (list_names[list_place[step]]), font=("Arial", 16, "normal"))
        elif step == 2:
            turName.write("3rd place: %s" % (list_names[list_place[step]]), font=("Arial", 16, "normal"))
        else:
            turName.write("%ith place: %s" % (step + 1, list_names[list_place[step]]), font=("Arial", 16, "normal"))

        turName.pendown()

    turName.penup()
    turName.goto(-670, 150)
    turName.write("Player's bet: %s" % (list_names[int(Player_Bet-1)]), font=("Arial", 16, "normal"))
    turName.pendown()
    turName.hideturtle()

def Ranking(list_ID_rank, list_names, list_time):
    ranking = turtle.Turtle()
    ranking.speed(0)
    for step in range(5):
        ranking.penup()
        ranking.goto(-620 + 260 * step, -300)
        ranking.pencolor("white")

        if step == 0:
            ranking.write("1st place: %s\n    %0.2f" % (list_names[list_ID_rank[step]], list_time[list_ID_rank[step]]), font=("Arial", 16, "normal"))
        elif step == 1:
            ranking.write("2nd place: %s\n    %0.2f" % (list_names[list_ID_rank[step]], list_time[list_ID_rank[step]]), font=("Arial", 16, "normal"))
        elif step == 2:
            ranking.write("3rd place: %s\n    %0.2f" % (list_names[list_ID_rank[step]], list_time[list_ID_rank[step]]), font=("Arial", 16, "normal"))
        else:
            ranking.write("%ith place: %s\n   %0.2f" % (step + 1, list_names[list_ID_rank[step]], list_time[list_ID_rank[step]]), font=("Arial", 16, "normal"))

        ranking.pendown()
        ranking.hideturtle()

