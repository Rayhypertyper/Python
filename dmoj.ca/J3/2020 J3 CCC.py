inputo = int(input())
arr = []
arr2 = []
arr3 = []
a = 0
for i in range(inputo):
    x = input()
    y = x.split(',')
    arr.append(y)

for i in range(inputo):
    arr2.append(arr[a][0])
    arr3.append(arr[a][1])
    a+=1
arr2.sort()
arr3.sort()
print(str(int(arr2[0])-1) + "," + str(int(arr3[0])-1))
print(str(int(arr2[-1])+1) + "," + str(int(arr3[-1])+1))


