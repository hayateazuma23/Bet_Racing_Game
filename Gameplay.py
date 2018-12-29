import Character_Implement
import RaceTrack
import Settings
import Announcement
import turtle
import random
import winsound
import time
import Score
import Chart

screen = turtle.Screen()

def play(length, width, choice, Player_Bet, list_score, list_bet_score):
    winsound.PlaySound("Music\\Racing.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    FinishLine = RaceTrack.Draw_RaceTrack(length, width)

    list_characters = Character_Implement.Settings_Characters(choice)
    list_shapes = Character_Implement.Setting_Shapes(choice, list_characters)
    list_names = [list_characters[0].Name, list_characters[1].Name, list_characters[2].Name,
                  list_characters[3].Name, list_characters[4].Name]

    list_rank = [0, 1, 2, 3, 4]
    random.shuffle(list_rank)
    list_place = [0, 0, 0, 0, 0]

    for step in range(5):
        for step2 in range(5):
            if list_rank[step2] == step:
                list_place[step] = step2

    RaceTrack.Arrange_Characters(list_characters, length, width, list_shapes, list_rank)
    RaceTrack.display_Name(list_names, list_place, Player_Bet)

    start_time = time.time()
    list_time = [0, 0, 0, 0, 0]

    while Settings.End_Match_Condition(list_characters, FinishLine) == 1:
        for ID in range(5):
            Character_Implement.Running(list_characters, list_shapes, ID, choice, FinishLine, list_time, start_time)


    for step in range(0, 5):
        if step != Settings.Check_Who_First(list_time)[0]:
            list_characters[step].Lose()
            Character_Implement.Losing(list_characters[step])

    Character_Implement.Winner(list_characters[Settings.Check_Who_First(list_time)[0]])

    list_ID_rank = Settings.Check_Who_First(list_time)

    Announcement.Annoucement(
        Settings.Win_Lose_Condition(Player_Bet, Settings.Check_Who_First(list_time)[0]), list_ID_rank, list_names, list_time)

    Score.Count_Score(list_ID_rank, list_score)
    Score.Count_Bet_Score(list_ID_rank, list_bet_score, Player_Bet)
    pass


def race():
    Settings.Setting_bg()
    x = turtle.Screen()
    length = x.numinput("Length of Race Track", "Input length of Race Track:(100-900)", 400, 100, 900)
    width = x.numinput("Width of Race Track", "Input width of Race Track:(300-400)", 400, 300, 400)
    choice = x.numinput("Choose Set Characters",
                        "There are 5 set of characters:\n  1.Animal\n  2.Marvel\n  3.Monsters\n  4.Pokemon\n  "
                        "5.SpaceShip\nInput number of the set you want to choose:",
                        1, 1, 5)

    list_characters = Character_Implement.Settings_Characters(choice)
    list_names = [list_characters[0].Name, list_characters[1].Name, list_characters[2].Name,
                  list_characters[3].Name, list_characters[4].Name]
    list_score = [0, 0, 0, 0, 0]
    list_bet_score = [0, 0, 0, 0, 0]

    Player_Bet = x.numinput("Place Your Bet", "Input the character you think will win:\n  1.%s\n  2.%s\n  3.%s\n  "
                                              "4.%s\n  5.%s" % (list_names[0], list_names[1], list_names[2],
                                                                list_names[3], list_names[4]), 1, 1, 5)

    play(length, width, choice, Player_Bet, list_score, list_bet_score)
    replay = x.numinput("Guess again", "Do you want to bet on your character again?\n yes(1) \n no(0):", 1, 0, 1)
    while replay == 1:
        play(length, width, choice, Player_Bet, list_score, list_bet_score)
        replay = x.numinput("Guess again", "Do you want to bet on your character again?\n yes(1) \n no(0):", 1, 0, 1)

    Chart.Chart(list_score, Score.Count_Win_Rate(list_bet_score), list_names)

