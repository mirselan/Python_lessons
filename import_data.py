import csv, json, os.path

def get_txt(data):
    with open('phone_numbers.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{data}''\n')


def get_csv(data):
    data_list = data.split(' ')
    with open('phone_numbers.csv', 'a', newline='') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(data_list)


def get_json(data):
    data_list = data.split(' ')
    dict_data = {}
    dict_data['Name'] = data_list[0]
    dict_data['Sername'] = data_list[1]
    dict_data['Phone'] = data_list[2]
    dict_data['Comments'] = data_list[3]
    if os.path.exists('phone_numbers.json'):
        with open('phone_numbers.json', encoding='UTF-8') as f:
            dicts = json.load(f)
        dicts.append(dict_data)
        with open('phone_numbers.json', 'w', encoding='UTF-8') as f:
            json.dump(dicts, f, indent=2)
    else:
        dict_list = []
        dict_list.append(dict_data) 
        with open('phone_numbers.json', 'w', encoding='UTF-8') as f:
            json.dump(dict_list, f, indent=2)