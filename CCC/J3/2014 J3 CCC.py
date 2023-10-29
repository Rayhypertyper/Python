x = int(input())
arr = []
antoniapoints = 100
davidpoints = 100
for i in range(x):
    y = input()
    arr.append(y.split()[0])
    arr.append(y.split()[1])
    if int(arr[0]) > int(arr[1]):
        davidpoints-=int(arr[0])
    elif int(arr[0]) < int(arr[1]):
        antoniapoints-=int(arr[1])
    elif int(arr[0]) == int(arr[1]):
        pass
    arr.clear()
print(antoniapoints)
print(davidpoints)