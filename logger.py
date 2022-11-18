from datetime import datetime


def log(data, type_data):
    time = datetime.now().strftime('%Y.%m.%d/%H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{type_data}: {data} -made at {time}''\n')
