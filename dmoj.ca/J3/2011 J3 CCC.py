x = int(input())
y = int(input())
arr = []
arr.append(x)
arr.append(y)
z = x - y
while z >= 0:
    arr.append(z)
    z = x - y
    x = y
    y = z
    z = x - y 
print(len(arr))
    
