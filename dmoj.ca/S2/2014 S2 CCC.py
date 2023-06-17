x = int(input())
dict = {}
y = input().split()
z = input().split()
for i in range(x):
    dict[y[i]] = z[i]
for key in dict:
    if dict[key] == key:
        print('bad')
        exit()
    if dict[dict[key]] == key:
        pass 
    else:
        print("bad")
        exit()
print("good")