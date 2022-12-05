import easygui as g


# Отрисовка поля
# def show_field(field):
#     print ("-------------")
#     for i in range(3):
#         print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
#         print ("-------------")


def show_field(field):
    msg = "-------------" + "\n"
    title = 'Cross - Zero Game'
    
    for i in range(3):
        msg_temp = ['|', ' ', str(field[0 + i * 3]), ' ', '|', 
        ' ', str(field[1 + i * 3]), ' ', '|', ' ', str(field[2 + i * 3]), ' ', '|', '\n']
        msg_2 = ''.join(msg_temp)
        msg += msg_2
        msg_3 = "-------------" + "\n"
        msg += msg_3
    g.msgbox(msg, title)