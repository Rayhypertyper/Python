# x = int(input())
# y = int(input())
# truecount = 0
# falsecount = 0
# arr = [ [False]*y for p in range (x)]
# z = int(input())
# for i in range(z):
#     e = list(input().split())
#     if e[0] == 'R':
#         for k in range(y):
#             arr[int(e[1])-1][k] = not arr[int(e[1])-1][k] 
#     elif e[0] == 'C':
#         for j in range(x):
#             arr[j][int(e[1])-1] = not arr[j][int(e[1])-1]
# h = sum(row.count(True) for row in arr)
# print(h)
rows = int(input())
cols = int(input())
x = int(input())
rowcount = 0
colcount = 0
arr = []
total = 0
for i in range(x):
    y = list(input().split())
    arr.append(y)
    if arr.count(y) % 2 == 0:
        arr.remove(y)
        arr.remove(y)
for i in arr:
    if i[0] == 'R':
        total+=cols
        rowcount+=1
    elif i[0] == 'C':
        total+=rows
        colcount+=1
print(total-(rowcount*colcount*2))