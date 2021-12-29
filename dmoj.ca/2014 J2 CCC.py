x = int(input())
arr = []
y = input()
A = 0
B = 0
z = 0
e = 0
for n in range(x):
    arr.append(y[e])
    e+=1

for m in range(x):
    if arr[z] == 'A':
        A+=1
    elif arr[z] == 'B':
        B+=1
    z+=1

if B > A:
    print('B')
elif A > B:
    print('A')
elif A == B:
    print("Tie")
    





