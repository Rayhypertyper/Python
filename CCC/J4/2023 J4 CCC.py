# x = int(input())
# y = input().split()
# z = input().split()
# arr = []
# brr = []
# boo = False
# coo = False
# count = 0
# dount = 0
# for i in range(x):
#     if y[i] == '1':
#         boo = True
#         count+=1
#     if boo:
#         if y[i] == '0':
#             arr.append(count)
#             count = 0
#             boo = False
#     if y[i] == '0':
#         arr.append(0)
#     if i + 1 == x and count > 0:
#         arr.append(count)
#     if z[i] == '0':
#         brr.append(0)
#     if z[i] == '1':
#         coo = True
#         dount+=1
#     if coo:
#         if z[i] == '0':
#             brr.append(dount)
#             dount = 0
#             coo = False
#     if i + 1 == x and dount > 0:
#         brr.append(dount)
    
# print(arr,brr)
        
#solution 2
x = int(input())
y = list(map(int, input().split()))
z = list(map(int, input().split()))
counter = 0
for i in range(x):
    if i >= 1:
        if y[i-1] == 0 and y[i] == 1:
            counter+=3
        elif y[i-1] == 1 and y[i] == 1:
            counter+=1
        if z[i-1] == 0 and z[i] == 1:
            counter+=3
        elif z[i-1] == 1 and z[i] == 1:
            counter+=1
    elif i == 0:
        if y[i] == 1:
            counter+=3
        if z[i] == 1:
            counter+=3
for i in range(x):
    if z[i] == 1 and y[i] == 1 and i%2 == 0:
        counter-=2
print(counter)
