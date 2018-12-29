def Count_Score(list_ID_rank, List_score):
    for step in range(5):
        List_score[list_ID_rank[step]] += 4 - step


def Count_Bet_Score(list_ID_rank, List_bet_score, Player_bet):
    for step in range(5):
        if list_ID_rank[step] == Player_bet - 1:
            List_bet_score[step] += 1


def Count_Win_Rate(List_bet_score):
    List_rate = [0, 0, 0, 0, 0]
    sum_of_scores = 0
    for stt in range(5):
        sum_of_scores += List_bet_score[stt]
    for i in range(5):
        List_rate[i] = (List_bet_score[i] / sum_of_scores) * 100
    return List_rate
