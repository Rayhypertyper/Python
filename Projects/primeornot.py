x = int(input())
for i in range(2,x):
    n = False
    for j in range(2,i):
        if i%j == 0:
            n = True
            break
    if n:
        continue
    print(i)

