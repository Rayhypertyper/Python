a = int(input())
x = input()
y = input()
b = 0
arr = []
brr = []
empty = 0
for i in range(a):
    arr.append(x[b])
    brr.append(y[b])
    b+=1
b = 0
for i in range(a):
    if x[b] == 'C' and y[b] == 'C':
        empty+=1
    b+=1

print(empty)