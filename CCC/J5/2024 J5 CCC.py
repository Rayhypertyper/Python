import sys
sys.setrecursionlimit(10**6)
x = int(input())
y = int(input())
arr = []

counter=0
for i in range(x):
    z = list(input())
    arr.append(z)
a = int(input())
b = int(input())
brr = [[False for i in range(y)] for j in range(x)]
def dfs(a,b, depth):
    global arr, counter, brr
    if a > x-1 or  b > y-1 or a < 0 or b < 0:
        depth-=1
        return
    if brr[a][b]:
        depth-=1
        return
    if arr[a][b] == "*":
        depth-=1
        return
    if arr[a][b] == 'S':
        counter+=1
        brr[a][b] = True
    elif arr[a][b] == 'M':
        counter+=5
        brr[a][b] = True
    elif arr[a][b] == 'L':
        counter+=10
        brr[a][b] = True
    dfs(a+1,b,depth+1)
    dfs(a-1,b,depth+1)
    dfs(a,b+1,depth+1)
    dfs(a,b-1,depth+1)
    return counter
print(dfs(a,b,0))