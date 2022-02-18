x = int(input())
y = int(input())
arr = [False]*x*y
z = int(input())
for i in range(z):
    e = list(input().split())
    if e[0] == 'R':
        for k in range(y):
            a = k+3*((int(e[1]))-1)
            print(a)
            if arr[a] == False:
                arr[k] = not arr[k]
            elif arr[a] == True:
                arr[k] = not arr[k]
    if e[0] == 'C':
        for j in range(z):
            b = j*3+int((arr[1])-1)
            if arr[b] == False:
                arr[b] = not arr[k]
            elif arr[b] == True:
                arr[b] = not arr[k]
for l in e:
    if l == True:
        l = 'G'
    elif l == False:
        l = 'B'