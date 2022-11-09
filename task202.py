num = int(input('Enter your number: '))
list_res = []

while num !=0:
    li = [i+1 for i in range(num)]
    res = 1
    for i in li:
        res *= i
    list_res.append(res)
    num -= 1

list_rev = list_res[:: -1]

print(list_rev)