# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов
##############################################################
# from random import uniform
# n = 5
# li = []

# for i in range(n):
#     el = round(uniform(0, 20), 2)
#     li.append(el)
# print(li)

li = [1.1, 1.2, 3.1, 5, 10.01]
li_cut = []
idx = 0
max_idx = 0
min_idx = 0
# Получаем список элементов без целой части
for i in range(len(li)):
    el = li[i] - int(li[i])
    if el != 0:
        li_cut.append(round(el, 2))
    else:
        continue
print(li_cut)
# Получаем индексы минимального и максимального элементов нового списка
while idx < len(li_cut):
    if li_cut[idx] > li_cut[max_idx]:
        max_idx = idx
    if li_cut[idx] < li_cut[min_idx]:
        min_idx = idx
    idx += 1
# Результат
res = li_cut[max_idx] - li_cut[min_idx]
print('%.2f' % res)