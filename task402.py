# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N
####################################################
n = int(input('Enter your number: '))
res = []
cur_num = n
prob = 2

while cur_num !=1:
    if cur_num % prob != 0:
        prob += 1
    else:
        cur_num /= prob
        res.append(prob)

print(res)
