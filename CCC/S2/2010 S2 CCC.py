x = int(input())
dict = {}
for i in range(x):
    y = input().split()
    dict[y[0]] = y[1]
z = list(input())
arr = []
for i in range(len(z)):
    for j in dict:
        if dict[j] == z[:len(dict[j])]:
            arr.append(j)
            for k in range(len(dict[j])):
                arr.pop(0)
            break
print(*arr)