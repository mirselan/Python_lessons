# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
#  и выведите на экран их сумму
################################################################
n = int(input('Enter integer number n: '))
set_dict = {}
res = 0

for i in range(1, n + 1):
    set_dict[i] = (1 + 1 / i) ** i
    res += set_dict[i]

print(round(res, 3))