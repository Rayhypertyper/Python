a = str(input())
b = str(input())
c = str(input())
d = str(input())
e = str(input())
f = str(input())

W = 0
L = 0

if(a == "W"):
    W = W + 1

if(b == "W"):
    W = W + 1
if(c == "W"):
    W = W + 1

if(d == "W"):
    W = W + 1

if(e == "W"):
    W = W + 1

if(f == "W"):
    W = W + 1


if(W == 1 or 2):
    print("3")
elif(W == 3 or 4):
    print("2")
elif(W == 5 or 6):
    print("1")