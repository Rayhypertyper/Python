# x = int(input())
# brr = []
# drr = []
# for i in range(x):
#     arr = list(input().split())
#     brr.append(arr)
# crr = brr[:]
# for k in range(x-1):
#     if brr[i][0] == 'R' and brr[i][1] == brr[i+1][1]:
#         drr.append(1)
#         k+=1
# print(brr)
# print(crr)


x = int(input())
arr = []
for i in range(x):
    y = list(input().split())
    arr.append(y)
brr = []
crr = []
for j in range(x):
    brr.append(arr[j][0])
    crr.append(arr[j][1])
    crr[j] = int(crr[j])
# drr = [l for l in crr if l not in drr]
tes = {l for l in crr}
drr = [n for n in tes]
err = []
for k in range(x):
    try:
        if crr[k] == crr[k+1] and brr[k] == 'R' and brr[k+1] == 'S':
            err.append(1)
            brr.pop(k)
            crr.pop(k)
        elif brr[k] == 'W':
            err.append(crr[k])
        else:
            err.append(1)
    except:
        pass
for j in range(x):
    az = 0
    
print(brr)
print(crr)
print(drr)
print(err)
print(sum(err))

