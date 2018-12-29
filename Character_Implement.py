import turtle
import random
import time
from Settings import Generate_Speed


def Get_name(choice):
    if (choice == 1):
        filename = "Characters\\Animal\\Name"
    elif (choice == 2):
        filename = "Characters\\Marvel\\Name"
    elif (choice == 3):
        filename = "Characters\\Monsters\\Name"
    elif (choice == 4):
        filename = "Characters\\Pokemon\\Name"
    elif (choice == 5):
        filename = "Characters\\SpaceShip\\Name"
    else:
        print("Can't find file !!")
    f = open(filename, "r")
    list_name = f.readlines()
    return list_name
    f.close()


def Settings_Characters(choice):
    if (choice == 1):
        list = [Animal(1, choice), Animal(2, choice), Animal(3, choice), Animal(4, choice), Animal(5, choice)]
    elif (choice == 2):
        list = [Marvel(1, choice), Marvel(2, choice), Marvel(3, choice), Marvel(4, choice), Marvel(5, choice)]
    elif (choice == 3):
        list = [Monster(1, choice), Monster(2, choice), Monster(3, choice), Monster(4, choice), Monster(5, choice)]
    elif (choice == 4):
        list = [Pokemon(1, choice), Pokemon(2, choice), Pokemon(3, choice), Pokemon(4, choice), Pokemon(5, choice)]
    elif (choice == 5):
        list = [SpaceShip(1, choice), SpaceShip(2, choice), SpaceShip(3, choice), SpaceShip(4, choice), SpaceShip(5, choice)]
    return list


def Setting_Shapes(choice,list):
    if (choice == 1):
        list_shapes = [list[0].Goat(), list[0].Fox(), list[0].Penguin(), list[0].Tiger(), list[0].Reindeer()]
    elif (choice == 2):
        list_shapes = [list[0].CaptainAmerica(), list[1].Deadpool(), list[2].IronMan(), list[3].IronPatriot(), list[4].StarLord()]
    elif (choice == 3):
        list_shapes = [list[0].Death(), list[1].Dragon(), list[2].Golem(), list[3].KasaObake(), list[4].Skull()]
    elif (choice == 4):
        list_shapes = [list[0].Raikou(), list[1].Reshiram(), list[2].Scrafty(), list[3].Serperior(), list[4].Zekrom()]
    elif (choice == 5):
        list_shapes = [list[0].Blue(), list[1].Green(), list[2].GreenPurple(), list[3].Purple(), list[4].Red()]
    return list_shapes


def Running (list_characters, list_shapes, ID, choice, FinishLine, list_time, start_time):
    if (list_characters[ID].character.xcor() < FinishLine):
        list_characters[ID].character.penup()
        Speed = Generate_Speed(choice)
        if (Speed > 0):
            list_characters[ID].character.shape(list_shapes[ID][4])
            list_characters[ID].character.forward(Speed)
            list_characters[ID].character.shape(list_shapes[ID][5])
            if (list_characters[ID].character.xcor() >= FinishLine):
                end_time = time.time()
                list_characters[ID].character.shape(list_shapes[ID][6])
                list_time[ID] = end_time-start_time
        elif(Speed < 0):
            list_characters[ID].character.shape(list_shapes[ID][2])
            list_characters[ID].character.backward(Speed)
            list_characters[ID].character.shape(list_shapes[ID][3])
        else:
            list_characters[ID].character.shape(list_shapes[ID][6])


def Losing(v):
    for step in range(0, 15):
        v.character.shape(v.list_lose[step])
    v.character.hideturtle()


def Winner(v):
    v.character.speed(6)
    v.character.penup()
    v.character.left(90)
    for step in range(0, 5):
        v.character.forward(50)
        v.character.backward(50)


class Character:
    def __init__(self, ID, choice):
        self.character = turtle.Turtle()
        self.screen = turtle.Screen()
        self.ID = ID
        self.list_Name = Get_name(choice)
        self.Name = self.list_Name[ID-1]
        self.screen.delay(100)

    def Lose(self):
        self.list_lose = ["Characters\\Losing\\explosion_1.gif",
                          "Characters\\Losing\\explosion_2.gif",
                          "Characters\\Losing\\explosion_3.gif",
                          "Characters\\Losing\\explosion_4.gif",
                          "Characters\\Losing\\explosion_5.gif",
                          "Characters\\Losing\\explosion_6.gif",
                          "Characters\\Losing\\explosion_7.gif",
                          "Characters\\Losing\\explosion_8.gif",
                          "Characters\\Losing\\explosion_9.gif",
                          "Characters\\Losing\\explosion_10.gif",
                          "Characters\\Losing\\explosion_11.gif",
                          "Characters\\Losing\\explosion_12.gif",
                          "Characters\\Losing\\explosion_13.gif",
                          "Characters\\Losing\\explosion_14.gif",
                          "Characters\\Losing\\explosion_15.gif"]
        for step in range (0, 15):
            self.screen.register_shape(self.list_lose[step])


class Marvel(Character):
    def Deadpool(self):
        self.list_deadpool = ["Characters\\Marvel\\Deadpool\\deadpool_left.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_right.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_RunLeft1.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_RunLeft2.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_RunRight1.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_RunRight2.gif",
                              "Characters\\Marvel\\Deadpool\\deadpool_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_deadpool[step])
        return self.list_deadpool

    def IronMan(self):
        self.list_ironman =["Characters\\Marvel\\Ironman\\ironman_left.gif",
                            "Characters\\Marvel\\Ironman\\ironman_right.gif",
                            "Characters\\Marvel\\Ironman\\ironman_runleft1.gif",
                            "Characters\\Marvel\\Ironman\\ironman_runleft2.gif",
                            "Characters\\Marvel\\Ironman\\ironman_runright1.gif",
                            "Characters\\Marvel\\Ironman\\ironman_runright2.gif",
                            "Characters\\Marvel\\Ironman\\ironman_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_ironman[step])
        return self.list_ironman

    def CaptainAmerica(self):
        self.list_captainamerica = ["Characters\\Marvel\\CaptainAmerica\\captainamerica_left.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_right.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_runleft1.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_runleft2.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_runright1.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_runright2.gif",
                                    "Characters\\Marvel\\CaptainAmerica\\captainamerica_standing.gif"]
        for step in range(0,7):
            self.screen.register_shape(self.list_captainamerica[step])
        return self.list_captainamerica

    def StarLord(self):
        self.list_starlord = ["Characters\\Marvel\\StarLord\\starlord_left.gif",
                              "Characters\\Marvel\\StarLord\\starlord_right.gif",
                              "Characters\\Marvel\\StarLord\\starlord_runleft1.gif",
                              "Characters\\Marvel\\StarLord\\starlord_runleft2.gif",
                              "Characters\\Marvel\\StarLord\\starlord_runright1.gif",
                              "Characters\\Marvel\\StarLord\\starlord_runright2.gif",
                              "Characters\\Marvel\\StarLord\\starlord_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_starlord[step])
        return self.list_starlord

    def IronPatriot(self):
        self.list_ironpatriot = ["Characters\\Marvel\\IronPatriot\\ironpatriot_left.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_right.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_runleft1.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_runleft2.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_runright1.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_runright2.gif",
                                 "Characters\\Marvel\\IronPatriot\\ironpatriot_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_ironpatriot[step])
        return self.list_ironpatriot


class Monster(Character):
    def Death(self):
        self.list_death = ["Characters\\Monsters\\Death\\death_left.gif",
                           "Characters\\Monsters\\Death\\death_right.gif",
                           "Characters\\Monsters\\Death\\death_runleft1.gif",
                           "Characters\\Monsters\\Death\\death_runleft2.gif",
                           "Characters\\Monsters\\Death\\death_runright1.gif",
                           "Characters\\Monsters\\Death\\death_runright2.gif",
                           "Characters\\Monsters\\Death\\death_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_death[step])
        return self.list_death

    def Dragon(self):
        self.list_dragon = ["Characters\\Monsters\\Dragon\\dragon_left.gif",
                            "Characters\\Monsters\\Dragon\\dragon_right.gif",
                            "Characters\\Monsters\\Dragon\\dragon_runleft1.gif",
                            "Characters\\Monsters\\Dragon\\dragon_runleft2.gif",
                            "Characters\\Monsters\\Dragon\\dragon_runright1.gif",
                            "Characters\\Monsters\\Dragon\\dragon_runright2.gif",
                            "Characters\\Monsters\\Dragon\\dragon_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_dragon[step])
        return self.list_dragon

    def Golem(self):
        self.list_golem = ["Characters\\Monsters\\Golem\\golem_left.gif",
                            "Characters\\Monsters\\Golem\\golem_right.gif",
                            "Characters\\Monsters\\Golem\\golem_runleft1.gif",
                            "Characters\\Monsters\\Golem\\golem_runleft2.gif",
                            "Characters\\Monsters\\Golem\\golem_runright1.gif",
                            "Characters\\Monsters\\Golem\\golem_runright2.gif",
                            "Characters\\Monsters\\Golem\\golem_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_golem[step])
        return self.list_golem

    def KasaObake(self):
        self.list_kasaobake = ["Characters\\Monsters\\Kasa-Obake\\kasaobake_left.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_right.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_runleft1.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_runleft2.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_runright1.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_runright2.gif",
                               "Characters\\Monsters\\Kasa-Obake\\kasaobake_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_kasaobake[step])
        return self.list_kasaobake

    def Skull(self):
        self.list_skull = ["Characters\\Monsters\\Skull\\skull_left.gif",
                           "Characters\\Monsters\\Skull\\skull_right.gif",
                           "Characters\\Monsters\\Skull\\skull_runleft1.gif",
                           "Characters\\Monsters\\Skull\\skull_runleft2.gif",
                           "Characters\\Monsters\\Skull\\skull_runright1.gif",
                           "Characters\\Monsters\\Skull\\skull_runright2.gif",
                           "Characters\\Monsters\\Skull\\skull_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_skull[step])
        return self.list_skull


class Animal(Character):
    def Fox(self):
        self.list_fox = ["Characters\\Animal\\Fox\\fox_left.gif",
                         "Characters\\Animal\\Fox\\fox_right.gif",
                         "Characters\\Animal\\Fox\\fox_runleft1.gif",
                         "Characters\\Animal\\Fox\\fox_runleft2.gif",
                         "Characters\\Animal\\Fox\\fox_runright1.gif",
                         "Characters\\Animal\\Fox\\fox_runright2.gif",
                         "Characters\\Animal\\Fox\\fox_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_fox[step])
        return self.list_fox

    def Goat(self):
        self.list_goat = ["Characters\\Animal\\Goat\\goat_left.gif",
                          "Characters\\Animal\\Goat\\goat_right.gif",
                          "Characters\\Animal\\Goat\\goat_runleft1.gif",
                          "Characters\\Animal\\Goat\\goat_runleft2.gif",
                          "Characters\\Animal\\Goat\\goat_runright1.gif",
                          "Characters\\Animal\\Goat\\goat_runright2.gif",
                          "Characters\\Animal\\Goat\\goat_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_goat[step])
        return self.list_goat

    def Penguin(self):
        self.list_penguin = ["Characters\\Animal\\Penguin\\penguin_left.gif",
                             "Characters\\Animal\\Penguin\\penguin_right.gif",
                             "Characters\\Animal\\Penguin\\penguin_runleft1.gif",
                             "Characters\\Animal\\Penguin\\penguin_runleft2.gif",
                             "Characters\\Animal\\Penguin\\penguin_runright1.gif",
                             "Characters\\Animal\\Penguin\\penguin_runright2.gif",
                             "Characters\\Animal\\Penguin\\penguin_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_penguin[step])
        return self.list_penguin

    def Tiger(self):
        self.list_tiger = ["Characters\\Animal\\Tiger\\tiger_left.gif",
                           "Characters\\Animal\\Tiger\\tiger_right.gif",
                           "Characters\\Animal\\Tiger\\tiger_runleft1.gif",
                           "Characters\\Animal\\Tiger\\tiger_runleft2.gif",
                           "Characters\\Animal\\Tiger\\tiger_runright1.gif",
                           "Characters\\Animal\\Tiger\\tiger_runright2.gif",
                           "Characters\\Animal\\Tiger\\tiger_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_tiger[step])
        return self.list_tiger

    def Reindeer(self):
        self.list_reindeer = ["Characters\\Animal\\Reindeer\\reindeer_left.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_right.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_runleft1.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_runleft2.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_runright1.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_runright2.gif",
                              "Characters\\Animal\\Reindeer\\reindeer_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_reindeer[step])
        return self.list_reindeer


class SpaceShip(Character):
    def Blue(self):
        self.list_blue = ["Characters\\SpaceShip\\Blue\\spaceshipblue_left.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_right.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_left.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_left.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_right.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_right.gif",
                          "Characters\\SpaceShip\\Blue\\spaceshipblue_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_blue[step])
        return self.list_blue

    def Red(self):
        self.list_red = ["Characters\\SpaceShip\\Red\\spaceshipred_left.gif",
                         "Characters\\SpaceShip\\Red\\spaceshipred_right.gif",
                         "Characters\\SpaceShip\\Red\\spaceshipred_left.gif",
                         "Characters\\SpaceShip\\Red\\spaceshipred_left.gif",
                         "Characters\\SpaceShip\\Red\\spaceshipred_right.gif",
                         "Characters\\SpaceShip\\Red\\spaceshipred_right.gif",
                         "Characters\\SpaceShip\\Green\\spaceshipgreen_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_red[step])
        return self.list_red

    def Green(self):
        self.list_green = ["Characters\\SpaceShip\\Green\\spaceshipgreen_left.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_right.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_left.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_left.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_right.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_right.gif",
                           "Characters\\SpaceShip\\Green\\spaceshipgreen_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_green[step])
        return self.list_green

    def Purple(self):
        self.list_purple = ["Characters\\SpaceShip\\Purple\\spaceshippurple_left.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_right.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_left.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_left.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_right.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_right.gif",
                            "Characters\\SpaceShip\\Purple\\spaceshippurple_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_purple[step])
        return self.list_purple

    def GreenPurple(self):
        self.list_greenpurple = ["Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_left.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_right.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_left.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_left.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_right.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_right.gif",
                                 "Characters\\SpaceShip\\GreenPurple\\spaceshipgreenpurple_standing.gif"]
        for step in range(0, 3):
            self.screen.register_shape(self.list_greenpurple[step])
        return self.list_greenpurple


class Pokemon(Character):
    def Reshiram(self):
        self.list_reshiram = ["Characters\\Pokemon\\Reshiram\\reshiram_left.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_right.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_runleft1.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_runleft2.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_runright1.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_runright2.gif",
                              "Characters\\Pokemon\\Reshiram\\reshiram_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_reshiram[step])
        return self.list_reshiram

    def Scrafty(self):
        self.list_scrafty = ["Characters\\Pokemon\\Scrafty\\scrafty_left.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_right.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_runleft1.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_runleft2.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_runright1.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_runright2.gif",
                             "Characters\\Pokemon\\Scrafty\\scrafty_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_scrafty[step])
        return self.list_scrafty

    def Zekrom(self):
        self.list_zekrom = ["Characters\\Pokemon\\Zekrom\\zekrom_left.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_right.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_runleft1.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_runleft2.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_runright1.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_runright2.gif",
                            "Characters\\Pokemon\\Zekrom\\zekrom_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_zekrom[step])
        return self.list_zekrom

    def Serperior(self):
        self.list_serperior = ["Characters\\Pokemon\\Serperior\\serperior_left.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_right.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_runleft1.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_runleft2.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_runright1.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_runright2.gif",
                               "Characters\\Pokemon\\Serperior\\serperior_standing.gif"]
        for step in range (0, 7):
            self.screen.register_shape(self.list_serperior[step])
        return self.list_serperior

    def Raikou(self):
        self.list_raikou = ["Characters\\Pokemon\\Raikou\\raikou_left.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_right.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_runleft1.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_runleft2.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_runright1.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_runright2.gif",
                            "Characters\\Pokemon\\Raikou\\raikou_standing.gif"]
        for step in range(0, 7):
            self.screen.register_shape(self.list_raikou[step])
        return self.list_raikou



