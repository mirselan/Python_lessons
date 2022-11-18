import csv, json, os.path


def from_txt(data):
    res = []
    with open('phone_numbers.txt', 'r', encoding='UTF-8') as f:
        res_list = f.readlines()
        for i in res_list:
            if data in i:
                res.append(i[:-1])
        if len(res) == 1:
            res = res[0]
             
    return res


def from_csv(data):
    #res = []
    with open('phone_numbers.csv', 'r', encoding='UTF-8', newline='') as f:
        res_csv = csv.reader(f, delimiter=' ')
        for i in res_csv:
            res_str = ''.join(i)
            if data in res_str:
                res = res_str
                break
            else:
                res = 'Not found'
    return res


def from_json(data):
    if os.path.exists('phone_numbers.json'):
        with open('phone_numbers.json', encoding='UTF-8') as f:
            temp_res = json.load(f)
        for i in temp_res:
            if data in i.values():
                res = i
                break
            else:
                res = 'Not found'
    else:
        res = 'json file not found'
             
    return res