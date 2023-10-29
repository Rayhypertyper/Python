x = int(input())
arr = []
brr = []
for i in range(x):
    y = int(input())
    arr.append(y)
arr.sort()
k = 1
calcs = 0
for j in range(len(arr) - 2):
    brr.append(float((arr[k] - arr[k - 1])/2) + float(((arr[k+1]-arr[k])/2)))
    k+=1
brr.sort()
print(brr[0])