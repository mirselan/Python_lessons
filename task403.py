# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
###################################################################################
from random import randint
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

with open('polynomial.txt', 'w', encoding='UTF-8') as f:
    f.write(res)
