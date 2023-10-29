x = int(input())
y = int(input())
xdbl = x
for i in range(y):
    xdbl += x*10
    x*=10
print(xdbl)