x = int(input())
arr = []
count = 0
for i in range(x):
    y = int(input())
    arr.append(y)
for i in range(int(x/2)):
    if arr[i] == arr[i+int(x/2)]:
        count+=1
print(count*2)