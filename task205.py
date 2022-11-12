# Реализуйте алгоритм перемешивания списка
##########################################
from random import randint
li = [1, 2, 3, 4, 5, 6]
li_res = []
old_idx = ''

while len(li_res) != len(li):
    idx = str(randint(0, 5))
    
    if idx not in old_idx:
        li_res.append(li[int(idx)])
    else:
        continue
    old_idx += idx

print(li_res)

