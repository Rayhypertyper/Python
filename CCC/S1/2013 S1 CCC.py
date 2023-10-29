x = int(input())
arr = set()
k = 0
x+=1
while True:
    for i in range(len(str(x))):
        arr.add(str(x)[k]) 
        k+=1
    if(len(str(x)) != len(arr)):
        x+=1
    elif len(str(x)) == len(arr):
        print(x)
        break
    arr.clear()
    k = 0
