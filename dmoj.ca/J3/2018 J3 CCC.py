x = input()
varnum = 0
arr = []
brr = []
lencalc = int(x.count(" ") + 1)
newlen = lencalc + 1
neulen = int((len(x) + 1)/2 - 1)
y = x.split()   
varnum = 0
varnumb = 0
print('0', end='')
print(" ", end='')
for k in range(lencalc):
    varnumb+=int(y[k])
    print(varnumb, end='')
    print(" ", end='')
    brr.append(varnumb)
brr.insert(0,0)
print('')
for l in range(int(newlen - 1)):
    varnumb = brr[l+1]
    for j in range(int(newlen)):    
        c = abs(int(varnumb) - int(brr[j]))
        print(c, end='')
        print(" ", end='')
    print('')