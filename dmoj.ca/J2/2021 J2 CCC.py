arr = []
numarr = []
numofppl = int(input())
if numofppl > 100:
  exit()
g = 1
unsortednumarr = []
f = 0
for i in range(numofppl):
  name = input()
  bidprice = int(input())
  arr.append(str(name))
  arr.append(bidprice)
  numarr.append(arr[g])
  g+=2

numarr.sort()
while True:
  if arr[f] == numarr[-1]:
    print(arr[f-1])
    break
  f+=1
