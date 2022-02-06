x = int(input())
arr = []
for i in range(x):
    y = int(input())
    arr.append(y)
    if y == 0:
        arr.pop(-1)
        arr.pop(-1)
b = sum(arr)
print(str(b))