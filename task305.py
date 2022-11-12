# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
##################################################
k = int(input('Enter how much digits will be in negaFibonacci chain: '))
first = 0
second = 1
res = '0 1 '
res_neg = '1 '

for i in range(k - 1):
    n = first + second
    
    first = second
    second = n
    res += str(n) + ' '

first = 0
second = 1

for i in range(k - 1):
    n = first - second
    
    first = second
    second = n
    res_neg += str(n) + ' '


fib = res_neg.split(' ')[::-1]
fibo = (','.join(fib).replace(',', ' ')) + ' ' + res

print(fibo)