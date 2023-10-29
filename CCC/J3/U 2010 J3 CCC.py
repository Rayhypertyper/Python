arr = input().split()
x = 0
y = 0
    while arr !='7':
    if int(arr[0]) == 1:
        if arr[1] == 'A':
            x = int(arr[2])
        elif arr[1] == 'B':
            y = int(arr[2])
    elif int(arr[0]) == 2:
        if arr[1] == 'A':
            print(x)
        elif arr[1] == 'B':
            print(y)
    elif int(arr[0]) == 3:
        if arr[1] == 'A':
            x = x+y
        elif arr[1] == 'B':
            y = x+y
    elif int(arr[0]) == 4:
        if arr[1] == 'A':
            x = x*y
        elif arr[1] == 'B':
            y = x*y
    elif int(arr[0]) == 5:
        if arr[1] == 'A':
            x = x-y
        elif arr[1] == 'B':
            y = x-y 
    elif int(arr[0]) == 6:
        if arr[1] == 'A':
            x = x/y
        elif arr[1] == 'B':
            y = x/y
    elif int(arr[0]) == 7:
        break
    arr = input().split()
    
    
           