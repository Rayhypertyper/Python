import sys
arr = [[0 -1], [0, -2],[0, -3],[1,-3],[2, -3],[3, -3],[3, -4],[3, -5],[4, -5],[5, -5],[5, -4],[5, -3],[6, -3],[7, -3],[7, -4],[7, -5],[7, -6],[7, -7],[6, -7],[5, -7],[4, -7],[3, -7],[2, -7],[1, -7],[0, -7],[-1, -7],[-1, -6],[-1, -5]]
cp = [-1,-5]
x = input().split()
while x[0] != "q":
    x[1] = int(x[1])
    if x[0] == 'u':
        for i in range(int(x[1])):
            cp[1]+=1
            if cp in arr:
                cp[1]-=(i+1)
                cp[1]+=x[1]
                print(*cp, "DANGER")
                sys.exit()
            arr.append(cp.copy())
    if x[0] == 'd':
        for i in range(int(x[1])):
            cp[1]-=1
            if cp in arr:
                cp[1]+=(i+1)
                cp[1]-=x[1]
                print(*cp, "DANGER")
                sys.exit()
            arr.append(cp.copy())
    if x[0] == 'l':
        for i in range(int(x[1])):
            cp[0]-=1
            if cp in arr:
                cp[0]+=(i+1)
                cp[0]-=x[1]
                print(*cp, "DANGER")
                sys.exit()
            arr.append(cp.copy())
    if x[0] == 'r':
        for i in range(int(x[1])):
            cp[0]+=1
            if cp in arr:
                cp[0]-=(i+1)
                cp[0]+=x[1]
                print(*cp, "DANGER")
                sys.exit()
            arr.append(cp.copy())
    print(*cp, "safe")
    x = input().split()
        
