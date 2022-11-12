# Вычислить число c заданной точностью d
########################################
from math import pi

precision = input('Enter precision(number d) from 10**(-1) to 10**(-10): ') # 10^{-1} ≤ d ≤10^{-10}
d_num = float(precision)

if 10**-1 >= d_num >= 10**-10: 
    pr_len = len((precision).split('.')[1])
    num = str(pi).split('.')
    num_res = num[0] + '.' + num[1][:pr_len]
    print(num_res)
else:
    print('Wrong number.')