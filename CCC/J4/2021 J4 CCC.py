x = input()
y = list(x)
lcount = 0
scount = 0
for i in range(len(x)):
    if y[i] == 'L':
        lcount+=1
    elif y[i] == 'S':
        scount+=1
    else:
        pass