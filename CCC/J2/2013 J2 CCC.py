x = input()
a = 0
b = 0
for i in range(len(x)):
    if x[a] == 'I' or x[a] == 'O' or x[a] == 'S' or x[a] == 'H' or x[a] == 'Z' or x[a] == 'X' or x[a] == 'N':
        b+=1
    else:
        print('NO')
        break
    a+=1
if b == len(x):
    print('YES')