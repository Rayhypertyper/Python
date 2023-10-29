x = int(input())
numtoletdict = {('A','B','C'):2, ('D','E','F'):3, ('G','H','I'):4, ('J','K','L'):5, ('M','N','O'):6, ('P','Q','R','S'):7, ('T','U','V'):8, ('W','X','Y','Z'):9}
for i in range(x):
    y = input().split('-')
    y = ''.join(y)
for i in range(len(y)):
    if y[i] in numtoletdict:
        y[i] = 
print(y)