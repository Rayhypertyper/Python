x = input()
a = 0
b = 1
c = 2
happycount = 0
sadcount = 0
if len(x) <= 2:
    print('none')
    exit()
for i in range(len(x)):
    if x[a] == ':' and x[b] == '-' and x[c] == ')':
        happycount+=1
    elif x[a] == ':' and x[b] == '-' and x[c] == '(':
        sadcount+=1
    a+=1
    b+=1
    c+=1
if happycount > sadcount:
    print('happy')
elif sadcount > happycount:
    print('sad')
elif happycount == 0 and sadcount == 0:
    print('none')
elif sadcount == happycount:
    print('unsure')
