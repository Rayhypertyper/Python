x = int(input())
y = list(map(int, input().split()))
arr = [0]
for i in range(1,x):
    lowest = float('inf')
    for j in range(x-i):
        total = 0
        for k in range(int((i+1)/2)):
            total+=abs(y[j:(j+i+1)][k] - y[j:(j+i+1)][-k-1])
        if total < lowest:
            lowest = total
    arr.append(lowest)
print(*arr)        
                
#Naive Solution

 

n = int(input())

mountains = list(map(int, input().split(" ")))

 

def calculateSymmetry(subList):

    sum = 0

 

    for i in range(len(subList)//2):

        sum += abs(subList[i] - subList[len(subList) - i - 1])

 

    return sum

 

print(0, end=" ")

 

for i in range(1, n): #Width of the photo

    minVal = 999999999999999999

    for j in range(n-i): #Starting index of the photo

        subList = mountains[j : j + i + 1]

        symmetry = calculateSymmetry(subList)

        minVal = min(minVal, symmetry)

    print(minVal, end=" ")
