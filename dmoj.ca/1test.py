inp = int(input())
arr = []
j = 0
l = 0
brr = []
crr = []
count = 0
for i in range(inp):
    x = input()
    a = int(len(x)) -1
    arr.append(x[0])
    for k in range(a):
        comp = x[j]
        j+=1
        if x[j] == comp:
            pass
        elif x[j] != comp:
            arr.append(x[j])
    for g in range(len(arr)):
        brr.append(x.count(arr[l]))
        brr.append(arr[l])
        l+=1
    v = len(arr) * 2 
    crr.append(v) 
    arr.clear()
    j = 0
    comp = ''
    l = 0
crr[0] = int(crr[0])-1
c = 0
b = int(crr[c])
h = 0
h+=b
print(*brr[l:b+1])
for u in range(inp-1):
    l = b + 1
    c+=1
    b = int(crr[c])
    h+=b
    b = h
    print(*brr[l:b+1])
# print(*brr[])



