li = [2, 3, 4, 5, 6]
res_li = []
idx_min = 0
idx_max = -1
count = 0

while idx_min < len(li) / 2:
    res_li.append(li[idx_min] * li[idx_max])
    idx_min +=1
    idx_max -=1

print(res_li)