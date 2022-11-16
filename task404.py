# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов
##################################################################
from random import randint
res_list = []
for i in range(2):
    k = input('Enter k-number: ')
    polynomial = 'x + y + 4 = 0'
    res = ''
    
    for i in polynomial:
        num = randint(0, 100)
        if i == 'x':
            res += str(num) + i + '^' + k
        elif i == 'y':
            res += str(num) + i + '^' + k
        else:
            res += i
    res_list.append(res)


for i in range(2):
    with open(f'polynomial_{i+1}.txt', 'w', encoding='UTF-8') as f:
        f.write(res_list[i])

polynom_list = []
for i in range(2):
    with open(f'polynomial_{i+1}.txt', 'r', encoding='UTF-8') as f:
        polynom = f.read()
        polynom_list.append(polynom)

print(polynom_list)

polinom_1 = polynom_list[0]
polinom_2 = polynom_list[1]
print(polinom_1, polinom_2)

temp_list_1 = polinom_1.split('+')
temp_list_2 = polinom_2.split('+')
print(temp_list_1, temp_list_2)

num_temp = ''
temp_list = []
for i in temp_list_1:
    for j in i:
        if j.isdigit():
            num_temp += j
            temp_list.append(num_temp)
        else:
            continue
print(temp_list)
