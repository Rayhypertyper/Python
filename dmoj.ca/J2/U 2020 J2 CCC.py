z = int(input())
x = int(input())
y = int(input())
yx = y/x
totalsumnumcases = x + y
daycount = 1
special = x
waycount = 0
h = 0
for i in range(z):
  waycount+=1
  if y == 1:
    x+=special
    if x > z:
      print(waycount)
      h+=1
      break

while y != 1:
  a = y*(yx)
  y = a
  totalsumnumcases+=y
  daycount+=1
  if totalsumnumcases > z:
    print(daycount)
    break
  

