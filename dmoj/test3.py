x = int(input())
y = int(input())
truecount = 0
falsecount = 0
arr = [ [False]*y for p in range (x)]
z = int(input())
for i in range(z*y):
    e = list(input().split())
    if e[0] == 'R':
        for k in range(y):
            arr[int(e[1])-1][k] = not arr[int(e[1])-1][k] 
    elif e[0] == 'C':
        for j in range(x):
            arr[j][int(e[1])-1] = not arr[j][int(e[1])-1]
h = sum(row.count(True) for row in arr)
print(h)