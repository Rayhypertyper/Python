x = int(input())
for i in range(x):
    y = input().split()
    if len(y[0]) <= 1 and len(y[1]) <= 1:
        print('NO')
    elif (y[0] == '7' and y[1][-1] == '1' and y[1][-1] == '1') or (y[0] == '11' and y[1][-1] == '7' and y[1][-2] != '1'):
        print('YES')
    elif y[0] == '17' or y[1] == '17' or (y[0][-1] == '7' and y[0][-2] == '1') or (y[1][-1] == '7' and y[1][-2] == '1'):
        print('NO')
    elif (y[0][-1] == '7' and y[1][-1] == '1' and y[1][-2] == '1') or (y[1][-1] == '7' and y[0][-1] == '1' and y[0][-2] == '1'):
        print('YES')
    else:
        print('NO')
    
    
    
    # elif :
    #     print('YES')
    # elif y[0] == '7' and y[1][-1] == '1' and y[1][-1] == '1' or y[0] == 11 and y[1][-1] == '7' and y[1][-2] != '1':
    #     print('YES')
    # elif y[0][-1] == '7' and y[1][-1] == '1' and y[1][-2] == '1' and y[0][-2] != '1' or (y[1][-1] == '7' and y[0][-1] == '1' and y[0][-2] == '1' and y[1][-2] != '1'):
    #     print('YES')
    # else:
    #     print('NO')