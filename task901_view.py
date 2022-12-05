from task901_constants import FIELD
import easygui as g


# Ввод игроками данных в игру
def take_input(player_token):
    valid = False
    while not valid:
        msg = "Куда поставим " + player_token + "?"
        player_answer = g.enterbox(msg)
        try:
            player_answer = int(player_answer)
        except:
            msg = "Некорректный ввод. Вы уверены, что ввели число?"
            g.msgbox(msg)
            continue
        if 1 <= player_answer <= 9:
            if (str(FIELD[player_answer-1]) not in "XO"):
                FIELD[player_answer-1] = player_token
                valid = True
            else:
                msg = "Эта клетка уже занята"
                g.msgbox(msg)
        else:
            msg = "Некорректный ввод. Введите число от 1 до 9 чтобы походить."
            g.msgbox(msg)