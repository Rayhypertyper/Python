x = list(input())
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
p = 0
arr = []
for i in range(len(x)):
    try:    
        if x[i] in a and x[i+1] in b:
            arr.append(x[p:i+1])
            p = i + 1
    except:
        arr.append(x[p:])    
for i in range(len(arr)):
    for k in range(len(arr[i])):
        if k == len(arr[i]) - 1:
            print(arr[i][k])
            break
        if arr[i][k] == '+':
            print(' tighten ', end='')
        if arr[i][k] == '-':
            print(' loosen ', end='')
        if arr[i][k] in a:
            print(arr[i][k], end='')
        elif arr[i][k]!= '+' and arr[i][k]!='-' and arr[i][k] not in a:
            print(arr[i][k], end='')