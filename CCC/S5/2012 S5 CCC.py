a = list(map(int, input().split()))
b = int(input())
arr = [[1 for _ in range(a[1])] for _ in range(a[0])] 
brr = []
crr = []
for i in range(b):
    c = list(map(int, input().split()))
    arr[c[0]-1][c[1]-1] = 0
    if int(c[0]) == 1:
        brr.append(c[1])
    if int(c[1]) == 1:
        crr.append(c[0])
if len(brr)>=1:
    brr.sort() #sorted list of posit ions of 0 in the first row
    for i in range(brr[0], a[1]):
        arr[0][i] = 0
if len(crr)>=1:
    crr.sort() #sorted list of positions of 0 in the first column
    for i in range(crr[0], a[0]):
        arr[i][0] = 0
for i in range(a[0]-1):
    for k in range(a[1]-1):
        if int(arr[i+1][k+1]) != 0:     
            arr[i+1][k+1] = arr[i+0][k+1]+arr[i+1][k+0]
print(arr[a[0]-1][a[1]-1])

