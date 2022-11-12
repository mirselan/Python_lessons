# Напишите программу, которая будет преобразовывать десятичное число в двоичное
###############################################################################
num = int(input('Enter the number: '))
res_temp = ''
res_dev = 0

while res_dev != 1:
    res_dev = num // 2
    trash_dev = num % 2
    num = res_dev
    res_temp += str(trash_dev)

res_temp += '1'
res = res_temp[:: -1]
print(res)
