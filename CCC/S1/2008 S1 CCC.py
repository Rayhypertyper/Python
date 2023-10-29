x = input().split()
lcity = x[0]
ltemp = int(x[1])
while x[0] != "Waterloo":
    x = input().split()
    if int(x[1]) < int(ltemp):
        ltemp = int(x[1])
        lcity = x[0]
print(lcity)