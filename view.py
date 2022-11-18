import import_data, export_data, logger

def get_import_mode(data, mode=1):
    if mode == 1:
        import_data.get_txt(data)
    elif mode == 2:
        import_data.get_csv(data)
    elif mode ==3:
        import_data.get_json(data)


def get_export_mode(data, mode=1):
    if mode == 1:
        return export_data.from_txt(data)
    elif mode == 2:
        return export_data.from_csv(data)
    elif mode == 3:
        return export_data.from_json(data)


def answer():
    mode = int(input('Enter 1 for txt, 2 for csv, 3 for json: '))
    data = input('Enter Second name: ')
    print(get_export_mode(data, mode))
    logger.log(data, 'Request')
    return data


def get_request():
    mode = int(input('Enter 1 for txt, 2 for csv, 3 for json: '))
    data = input('Enter First_name, Second_name, Phone_number and your comments with space: ')
    if ' ' not in data:
        print('You have to put space between values.')
        get_request()
    get_import_mode(data, mode)
    logger.log(data, 'Record')