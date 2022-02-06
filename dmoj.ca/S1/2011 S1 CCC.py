x = int(input())
scount = 0
tcount = 0
for i in range(x):
    y = input()
    arr = list(y)
    for k in range(len(arr)):
        if arr[k] == 't' or arr[k] == 'T':
            tcount+=1
        if arr[k] == 's' or arr[k] == 'S':
            scount+=1
    arr.clear()
if scount > tcount or scount == tcount:
    print('French')
elif scount < tcount:
    print('English')