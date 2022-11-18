import view


def user_mode():
    mode = input('Enter EX for export and IM for import phone numbers: ')
    if 'im'.casefold() in mode:
        view.get_request()
    elif 'ex'.casefold() in mode:
        view.answer()
    else:
        print('Just EX or IM is correct.')
    is_exit = input('Enter exit, if want to leave the program or push enter button to stay in: ')
    if 'exit' not in is_exit:
        user_mode()
    else:
        return
