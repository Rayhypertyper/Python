# x = int(input())
# gates = [False for i in range(x+1)]
# y = int(input())
# counter = 0
# arr = []
# boo = False
# for i in range(y):
#     z = int(input())
#     arr.append(z)
# for i in arr:
#     for j in range(i,0,-1):
#         if not gates[j]:
#             gates[j] = True
#             break
#         if j == 1:
#             boo = True
#     if boo:
#         break
# for i in gates:
#     if i:
#         counter+=1
# print(counter)
# for i in range(y):
#     z = int(input())
#     c = [i for i in range(z)]
#     if c not in dicto:
#         dicto[c] = 1
#     else:
#         dicto[c]+=1
# sorteddict = dict(sorted(len(dicto.items())))
# for i in sorteddict:
#     for j in sorteddict[i]:
#         if not gates[j]:
#             gates[j] = True
# for i in gates:
#     if i:
#         counter+=1
# print(counter)


#new solutoin
x = int(input())
gates = [False for i in range(x)]
y = int(input())
for i in range(y):
    z = int(input())
    