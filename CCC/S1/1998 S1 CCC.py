x = int(input())
for i in range(x):
    x = input().split()
    for i in range(len(x)): 
        if len(x[i]) == 4:
            x[i] = "****"
    print(*x)
