x = input() 
y = input() 
reference = list(x) 
reference2 = list(y)
arr = [] 
g = 0 
r = 0
for i in range(len(x) - len(y) + 1): 
    for k in range(len(y)): 
        arr.append(reference[g])
        g+=1 
        arr.sort() 
    reference2.sort()
    if arr == reference2:
        r+=1
        print('yes')
        break
    g-=len(y) - 1
    arr.clear()
if r == 0: 
    print('no')

  
  