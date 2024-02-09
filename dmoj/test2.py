# # a = 1
# # b = 1
# # c = 1
# # count = 0
# # for i in range(10):
# #   a+=1
# #   b = 0
# #   for j in range(10):
# #     b+=1
# #     c = 0
# #     for k in range(10):
# #       c+=1
# #       if a+b+c <= 10:
# #         count+=1
# # print(count)
# arr = [[1,2],[2,3],[3,4],[4,5]]
# # for o in arr:
# #   print(o)

# for i in arr:
#   print(i)
#   print('hi')
#   print(i)
# x = int(input())
# for i in range(x+1,1000000):
#     for j in str(i):
#         k = 0
#         if j == '0':
#             k = 1
#             break
#     if k == 0:
#         print(i)
#         break

# a = [1, 0, 1]
# count = 0
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         for k in range(1,len(a)+1):
#             if a[j:k].count(1) > a[j:k].count(0):
#                 print(a[j:k])
#                 count+=1
# print(count)

a = {13:12, 23:22, 33:32}
for i in a:
    print(i)