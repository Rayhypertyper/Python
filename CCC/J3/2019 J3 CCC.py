x = int(input())
brr = [] 
for k in range(x):
    y = input()
    arr = list(y)
    brr.append(arr[0])
    for i in range(len(arr)): 
        try:
            if arr[i] != arr[i+1]: 
                print(brr.count(arr[i]), arr[i], end='')
                print(' ', end='')
                brr.clear()
            brr.append(arr[i+1]) 
        except:
            pass
    print(brr.count(arr[-1]), arr[i])   
    brr.clear()