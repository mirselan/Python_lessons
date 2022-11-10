from math import pi

precision = input('Enter precision(number d): ')

pr_len = len((precision).split('.')[1])
num = str(pi).split('.')
num_res = num[0] + '.' + num[1][:pr_len]
print(num_res)