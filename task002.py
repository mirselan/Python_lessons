x = int(input('Enter first coordinate: '))
y = int(input('Enter second coordinate: '))
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)
else:
    print('It\'s a wrong coordinates')
