x = str(input())
y = ''
while x != '99999':
    if (int(x[0]) + int(x[1]))%2 == 0 and (int(x[0]) + int(x[1])) != 0:
        y = 'right'
        print('right', end=' ')
        print(x[2], end='')
        print(x[3], end='')
        print(x[4])
    elif (int(x[0]) + int(x[1])) == 0:
        print(y, end=' ')
        print(x[2], end='')
        print(x[3], end='')
        print(x[4])
    else:
        y = 'left'
        print('left', end=' ')
        print(x[2], end='')
        print(x[3], end='')
        print(x[4])
    x = str(input())