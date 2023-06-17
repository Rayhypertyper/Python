import sys
x = int(input())
arr = []
y = int(input())
for i in range(y):
    z = int(input())
    arr.append(z)
count = 0
counter = 0
if y <= 3:
    for i in arr:
        if count > x:
            break
        count+=i
        counter+=1
    print(counter-1)
else:
    for i in range(4):
        if count > x:
            print(i-1)
            sys.exit()
        count+=arr[i]
    for i in range(len(arr)-3):
        if sum(arr[i:i+4]) > x:
            print(3+i)
            break
        if i == len(arr)-4:
            print(y)