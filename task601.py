# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов
##############################################################
li = [1.1, 1.2, 3.1, 5, 10.01]
idx = 0
max_idx = 0
min_idx = 0
# Получаем список элементов без целой части-list comprehension
li_cut = [round((i - int(i)), 2) for i in li if (i - int(i)) != 0]
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