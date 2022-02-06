arr = ['1','2','3','4']
x = input()
brr = list(x)
for i in range(len(brr)):
    if brr[i] == 'H':  
        arr.append(arr[0])
        arr.append(arr[1])
        arr.pop(0)
        arr.pop(0)
    elif brr[i] == 'V':
        arr.insert(0, arr[1])
        arr.insert(5, arr[3])
        arr.pop(2)
        arr.pop(2)
print(arr[0], arr[1])
print(arr[2], arr[3])