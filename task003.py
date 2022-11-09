area_num = input('Enter number of coordinate quarter: ')
if area_num == '1':
    print('0 < X < +infinity and 0 < Y < +infinity.')
elif area_num == '2':
    print('-infinity < X < 0 and 0 < Y < +infinity.')
elif area_num == '3':
    print('-infinity < X < 0 and -infinity < Y < 0.')
elif area_num == '4':
    print('0 < X < +infinity and -infinity < Y < 0.')
else:
    print('It\'s a wrong number of quarter.')