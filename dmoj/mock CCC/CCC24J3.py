a = int(input())
b = list(input())
arr = [0]
boo = False
counter = 0
for i in range(len(b)):
    if i != len(b):
        if b[i] == "G" and b[i+1] == "G":
            boo = True
    if boo:
        boo = False
        continue
    if b[i] == "G":
        arr.append(i)
for i in range(len(arr)-2):
    counter+=(b[arr[i]:arr[i+1]].count("R")*b[arr[i+1]:arr[i+2]].count("B"))
print(counter)