from datetime import datetime
import os.path


# def log(data, type_data):
#     time = datetime.now().strftime('%Y.%m.%d/%H:%M')
#     with open('log.txt', 'a', encoding='UTF-8') as f:
#         f.write(f'{type_data}: {data} -made at {time}''\n')


def log_menu(data):
    time = datetime.now().strftime('%Y.%m.%d/%H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(f'Пользователь(id: {str(data.from_user.id)}) выбрал пункт меню - {str(data.text)} (made at {time})''\n')


def log_mode(data):
    time = datetime.now().strftime('%Y.%m.%d/%H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(f'Пользователь: {str(data.chat.first_name)} {str(data.chat.last_name)} выбрал режим: {str(data.text)} (made at {time})''\n')


def log_user_requests(mode, data):
    time = datetime.now().strftime('%Y.%m.%d/%H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(f'Пользователь: {str(data.chat.first_name)} {str(data.chat.last_name)} выбрал формат: {mode} и ввёл данные {str(data.text)} (made at {time})''\n')


# def log_operations(data, value):
#     time = datetime.now().strftime('%Y.%m.%d/%H:%M')
#     with open('log.txt', 'a', encoding='UTF-8') as f:
#         f.write(f'Пользователь: {str(data.message.chat.first_name)} {str(data.message.chat.last_name)}, Запрос пользователя: {str(data.message.text)}, Ответ системы: {str(value)} (made at {time})''\n')


def read_log():
    if os.path.exists('log.txt'):
        with open('log.txt', 'r', encoding='UTF-8') as f:
            res = f.read()
    else:
        res = 'log file not found.'
    return res