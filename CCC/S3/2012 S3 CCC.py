x = int(input())
arr = []
seto = set()
firstlist = []
scndlist = []
for i in range(x):
    y = int(input())
    arr.append(y)
my_dict = {}
for i in arr:
    if i not in my_dict:
        my_dict[i] = 1
    elif i in my_dict:
        my_dict[i]+=1
for i in my_dict:
    seto.add(my_dict[i])
seto = sorted(list(seto))
for i in my_dict:
    if my_dict[i] == seto[-1]:
        firstlist.append(i)
    elif my_dict[i] == seto[-2]:
        scndlist.append(i)
if len(firstlist) >= 2:
    firstlist.sort()
    print(abs(firstlist[0]-firstlist[-1]))
else:
    scndlist.sort()
    if abs(firstlist[0] - scndlist[0]) > abs(firstlist[0] - scndlist[-1]):
        print(abs(firstlist[0] - scndlist[0])) 
    elif abs(firstlist[0] - scndlist[0]) < abs(firstlist[0] - scndlist[-1]):
        print(abs(firstlist[0] - scndlist[-1]))




    

# num = list(set(valueslist.count(valueslist[0])))
# for i in my_dict:
#     if my_dict[i] == num[0]:
#         crr.append(str(i) + " " + str(my_dict(i)))
#     elif my_dict[i] == num[1]:
#         drr.append(str(i) + " " + str(my_dict(i)))
#     else:
#         break
# print(crr)
# print(drr)
# if num == 1:
# if num == 2:
#     print(abs())
# for i in my_dict:
#     crr.append()
# print(my_dict)
# arr = []
# letteracount = 0
# lettera = 
# letterbcount =
# letterb =
# x = int(input())
# for i in range(x):
#     y = input()
#     arr.append(y)
# arr.sort()
# for i in range(len(arr)):
#     if 
#     letteracount = arr[i]

