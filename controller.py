import view
import easygui as g


def user_mode():
    msg = 'Chose what you want to do with DataBase'
    title = 'Chosing working mode of DataBase'
    choices = ['INSERT', 'SELECT', 'UPDATE', 'DELETE']
    mode = g.choicebox(msg, title, choices)
    if mode == 'INSERT':
        view.request()
    elif mode == 'SELECT':
        view.answer()
    elif mode == 'UPDATE':
        view.change()
    elif mode == 'DELETE':
        view.remove()
    msg_2 = 'Do you want to continue?'
    title_2 = 'Please confirm'
    is_exit = g.ccbox(msg_2, title_2)
    if is_exit:
        user_mode()
    else:
        return

    