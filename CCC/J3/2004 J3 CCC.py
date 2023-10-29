x = int(input())
y = int(input())
z = x * y
a = []
b = []
c = 0
d = 0
for i in range(x):
  adjword = input()
  a.append(adjword)

for j in range(y):
  nounword = input()
  b.append(nounword)

for k in range(z):
    print(a[c] + " as " + b[d])
    d+=1
    if d == y:
        d = 0
        c +=1





