x = int(input())
y = input().split()
z = input().split()
arr = []
brr = []
boo = False
coo = False
count = 0
dount = 0
for i in range(x):
    if y[i] == '1':
        boo = True
        count+=1
    if boo:
        if y[i] == '0':
            arr.append(count)
            count = 0
            boo = False
    if y[i] == '0':
        arr.append(0)
    if i + 1 == x and count > 0:
        arr.append(count)
    if z[i] == '0':
        brr.append(0)
    if z[i] == '1':
        coo = True
        dount+=1
    if coo:
        if z[i] == '0':
            brr.append(dount)
            dount = 0
            coo = False
    if i + 1 == x and dount > 0:
        brr.append(dount)
    
print(arr,brr)
        