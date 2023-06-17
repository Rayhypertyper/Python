# # arr = []
# # brr = []
# # crr = []
# # myseta = set()
# # mysetb = set()
# # mysetc = set()
# # count = 0
# # x = int(input())
# # for i in range(x):
# #     a = tuple(input().split())
# #     arr.append(a)
# # y = int(input())
# # for i in range(y):
# #     b = tuple(input().split())
# #     brr.append(b)
# # z = int(input())
# # for i in range(z):
# #     c = tuple(input().split())
# #     mysetc.add(c)
# # for i in mysetc:
# #     for k in arr:
# #         if k in i:
# #             pass
# #         else:
# #             count+=1
# #             break
# # print(count)
# arr = []
# brr = []
# crr = []
# count = 0
# x = int(input())
# for i in range(x):
#     a = list(input().split())
#     arr.append(a)
# y = int(input())
# for i in range(y):
#     b = list(input().split())
#     brr.append(b)
# z = int(input())
# for i in range(z):
#     c = list(input().split())
#     crr.append(c)
# for i in range(len(arr)):
#     for j in range(len(crr)):
#         if arr[i][0] in crr[j]:
#             if arr[i][1] in crr[j]:
#                 pass
#             else:
#                 count+=1     
# for l in range(len(brr)):
#     for k in range(len(crr)):
#         if brr[l][0] in crr[k]:
#             if brr[l][1] in crr[k]:
#                 count+=1
#             else:
#                 pass
# print(count)


# # for i in range(len(arr)):
# #     for j in range(len(myset)):
# #         if arr[i][0] in crr[j]:
# #             if arr[i][1] in crr[j]:
# #                 pass
# #             else:
# #                 count+=1     
# # for l in range(len(brr)):
# #     for k in range(len(crr)):
# #         if brr[l][0] in crr[k]:
# #             if brr[l][1] in crr[k]:
# #                 count+=1
# #             else:
# #                 pass
# # print(count)
x = int(input())
arr = []
my_dict = dict()
my_dikt = dict()
for i in range(x):
    inp = input().split()
    my_dict[inp[0]] = inp[1]
    my_dict[inp[1]] = inp[0]
y = int(input())
for i in range(y):
    inpt = input().split()
    my_dikt[inpt[0]] = inpt[1]
    my_dikt[inpt[1]] = inpt[0]
z = int(input())
for i in range(z):
    g = input().split()
    arr.append(g)
print(arr)
print(my_dict)
print(my_dikt)
    




# print()
# for i in range(len(arr)):
#     for a,b in my_dict.item():
#         if 

        



