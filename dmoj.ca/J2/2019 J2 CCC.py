x = int(input())
arr = []
strr = []
str2 = []
a = 0
b = 1

for i in range(x):
    y = input()
    arr.append(y.split()[0])
    arr.append(y.split()[1])
    print(int(arr[a]) * arr[b])
    a+=2
    b+=2
# for i in range(x):
    


