x = int(input())
for i in range(x):
    count = 0
    y = int(input())
    z = list(map(int, input().split()))
    for j in range(y-1):
        while z[j+1] <= z[j]:
            z[j+1]*=10
            count+=1
    print(("Case " + "#" + str(int(i+1))) + ": " + str(count))
        

