x = int(input())
arr = []
counter = 0
for i in range(x*2):
    y = input()
    arr.append(y)
for k in range(x):
    if arr[k] == arr[k+x]:
        counter+=1
print(counter)