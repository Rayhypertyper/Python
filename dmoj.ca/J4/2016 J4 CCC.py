x = list(map(int, input().split(':')))
counter = 0
for i in range(12):
    if x[0] >= 7 and x[0] <=9:
        counter+=10
    elif x[0] >= 15 and x[1] <=19:
        x[1]+=10
    if x[0] == 23 and x[1] == 60:
        x[0] = 0
        x[1] = 0        
    if x[1] == 60:
        x[0]+=1
        x[1] = 0
    counter+=10
    if x[0] == 23 and x[1] == 60:
        x[0] = 0
        x[1] = 0    
    if x[1] == 60:
        x[0]+=1
        x[1] = 0

g = [str(c) for c in x]

a = int(counter/60)
b = counter - (60*a)
if len(g[0]) == 1 and len(g[1]) == 1:
    print('0' + g[0] + ':' + '0' + g[1])
elif len(g[0]) == 1 and len(g[1]) == 2:
    print('0' + g[0] + ':' + g[1])
elif len(g[0]) == 2 and len(g[1]) == 1:
    print(g[0] + ':' + '0' + g[1])
elif len(g[0]) == 2 and len(g[1]) == 2:
    print(g[0] + ':' + g[1])
