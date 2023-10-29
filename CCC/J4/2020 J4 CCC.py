x = list(input()) 
y = list(input())
stop = False
for i in range(len(x) - len(y) + 1):
    arr = x[i:(i+len(y))]
    for k in range(len(y)):
        if arr == y:
            print('yes')
            stop = not stop
            break
        arr.append(arr[0])
        arr.pop(0)
    if stop == True:
        break
if stop == False:
    print('no')











  
