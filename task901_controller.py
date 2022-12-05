import task901_showField, task901_checkWin, task901_view
import easygui as g


def controller(field):
    counter = 0
    win = False
    while not win:
        task901_showField.show_field(field)
        if counter % 2 == 0:
            task901_view.take_input("X")
        else:
            task901_view.take_input("O")
        counter += 1
        if counter > 4:
            tmp = task901_checkWin.check_win(field)
            if tmp:
                msg = tmp + " " + "выиграл!"
                g.msgbox(msg)
                win = True
                break
        if counter == 9:
            msg = "Ничья!"
            g.msgbox(msg)
            break
    task901_showField.show_field(field)