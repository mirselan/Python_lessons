number = input('Enter your number: ')
num_list = [int(i) for i in number if i.isdigit()]
print(sum(num_list))
