x = int(input())
y = int(input())
z = 0
b = 1
factorcounter = 0
numcounter = 0
v = x - 1
k = x
t = x

for c in range(x):
  if x % b == 0:
    factorcounter+=1
  b+=1
  if factorcounter == 4 and x == k:
    factorcounter == 0
    numcounter+=1

  if x == b:
    x+=1
    k+=1
    b = 1
  if x == y:
    break
 