x = int(input())
y = list(map(int, input().split()))
y.insert(0,0)
max = 0
brr = []
for i in range(1,x+1):
    for j in range(1+i,x+2):
        arr = y[i:j]
        sum = float(1)
        for k in arr:
            sum*=k
        sum=sum/(j-i)
        if sum>max:
            max = sum
            brr = [i,j-1]
print(*brr)



        
