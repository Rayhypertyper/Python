x = list(input())
row = int(input())
col = int(input())
arr = []
count = 0
for i in range(row):
    rows = input().split()
    arr.append(rows)
for i in range(row):
    for j in range(col-len(x)+1):
        if list(arr[i][j:len(x)+j]) == x or list(reversed(arr[i][j:len(x)+j])) == x:
            count+=1
# print('')
# for j in range(col):
#     for i in range(row-len(x)+1):
#         print(list(arr[j][i:len(x)+i]))
#         print(list(reversed(arr[j][i:len(x)+i])))
#         print(x)
#         if list(arr[j][i:len(x)+i]) == x or list(reversed(arr[j][i:len(x)+i])) == x:
#             count+=1

print(count)

#only 2/15 points
        