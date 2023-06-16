x = int(input())
for i in range(x):
    y = list(map(int, input().split()))
    z = list(map(int, input().split()))
    z = sum(z)
    a = int(z/y[1])
    print(("Case " + "#" + str(int(i+1))) + ": " + str(int(z-a*y[1])))