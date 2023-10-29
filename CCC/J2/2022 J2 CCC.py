arr = []
x = int(input())
for i in range(x*2):
    y = int(input())
    arr.append(y)
z = 0
gold = 0
for k in range(x):
    if (arr[z]* 5) - (arr[z+1] * 3) > 40:
        gold+=1
    z+=2
if gold == x:
    print(x, end ='')
    print("+")
elif gold != x:
    print(gold)