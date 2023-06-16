# 
x = int(input())
arr = ['a','e','i','o','u','A','E','I','O','U']
for i in range(x):
    y = input()
    if y[-1] in arr: 
        print(("Case " + "#" + str(int(i+1))) + ": " + str(y) + " is ruled by Alice.")
    elif y[-1] == 'y':
        print(("Case " + "#" + str(int(i+1))) + ": " + str(y) + " is ruled by nobody.")
    else: 
        print(("Case " + "#" + str(int(i+1))) + ": " + str(y) + " is ruled by Bob.")