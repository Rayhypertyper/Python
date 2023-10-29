x = list(map(int, input().split()))
arr = []
for i in range(x[0]):
    npt = list(input())
    arr.append(npt)
try:
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            if arr[i][j] == 'W' and arr[i] == 0 and arr[i+1][j] != 'C' or arr[i+1][j] != 'W':
                



# y = [[0 for i in range(x[1])] for j in range(x[0])]
# try:
