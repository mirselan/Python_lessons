day = int(input('Enter day number: '))
if 0 < day < 8 and type(day) == int:
    if day == 6 or day == 7:
        print('Yes')
    else:
        print('No')
else:
    print('Were is no such day number in 7-day week. ')