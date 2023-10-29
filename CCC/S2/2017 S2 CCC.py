x = int(input())
y = list(map(int, input().split()))
y.sort()
g = ''
if x % 2 == 1:
    g=y[0]
    y.pop(0)
arr = []
a = int(x/2)
y.reverse()
for j in range(int(x/2), x-(x%2)):
    arr.append(y[j])
y.reverse()
for i in range(int(x/2), x-(x%2)):
    arr.append(y[i])
if x % 2 == 1:
    pass
for k in range(int(x/2)):
    print(arr[k], end=' ')
    print(arr[k+a], end=' ')
print(g)