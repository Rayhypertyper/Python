x = int(input())
swiscr = 0
semascr = 0
b = 0
y = input()
z = input()
arr = y.split()
brr = z.split()
for i in range(x):
    swiscr+=int(arr[i])
    semascr+=int(brr[i])
    if swiscr == semascr:
        b = i+1
print(b)