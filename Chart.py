import matplotlib.pyplot as plt


def Chart(List_Score, list_sizes, list_names):
    Char_score = {list_names[0]: List_Score[0], list_names[1]: List_Score[1], list_names[2]: List_Score[2],
                  list_names[3]: List_Score[3], list_names[4]: List_Score[4]}

    Scores = sorted(Char_score.values(), reverse=True)
    # Sort các nhân vật dựa và số điểm (giảm dần)
    Characters = sorted(Char_score, key=Char_score.__getitem__, reverse=True)

    # Chỉ số các nhân vật
    ind_Chars = range(len(Char_score))

    # Vẽ biểu đồ cột
    plt.bar(ind_Chars, Scores, align='center')
    plt.xticks(ind_Chars, Characters)

    # Label x, y axit
    plt.xlabel('Characters')
    plt.ylabel('Score')
    # Label title of bar char
    plt.title('SCORE OF CHARACTERS')

    # Thêm các giá trị trên mỗi cột
    for x, y in zip(ind_Chars, Scores):
        plt.text(x + 0.02, y + 0.05, '%d' % y, ha='center', va='bottom')

    # Tăng trục y thêm 20 đơn vị
    plt.ylim(0, Scores[0] + 20)

    # Kết quả:
    #plt.show()

    labels = '1st', '2nd', '3th', '4th', '5th'
    explode = (0.1, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(list_sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)

    ax1.axis('equal')
    plt.title("FINISHED RATE BASE ON YOUR CHARACTER'S RANK")
    plt.show()
    plt.disconnect()


