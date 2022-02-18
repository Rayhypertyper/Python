a = input()
b = int(input())
arr = input().split()
brr = input().split()
sum = 0
for c in range(b):
    arr.append(int(arr[0]))
    arr.pop(0)
for d in range(b):
    brr.append(int(brr[0]))
    brr.pop(0)
arr.sort()
brr.sort()
if a == '1':
    for i in range(b):
        sum+=max(int(arr[i]), int(brr[i]))
if a == '2':
    for k in range(b):
        sum+=max(int(arr[k]), int(brr[-k-1]))
print(sum)