# x = int(input())
# y = int(input())
# arr = []
# brr = []
# seto = {1,2}
# seto.clear()
# for i in range(y):
#     z = list(map(int, input().split()))
#     arr.append(z[0])
#     arr.append(z[1])
#     arra = z[0],z[1]
#     brr.append(z)
#     seto.add(arra)
# grr = seto.copy()
# grea,test = 0,0
# d = 1000000000
# a,b = 0,0
# if x%2 == 1:
#     a,b = (x+1)/2,(x+1)/2
# elif x%2 == 0:
#     a,b = x/2,x/2
# for j in range(int(len(arr)/2)):
#     if abs(arr[j*2]-a)+abs(arr[j*2+1] - b) < d:
#         d = abs(arr[j*2]-a)+abs(arr[j*2+1] - b)
#         grea,test = arr[j*2],arr[(j*2)+1]
# counter = 0
# count = 0
# crr = []
# e = x - min(grea,test)
# for k in range(e+1):
#     for l in range(k):
#         for m in range(k):
#             onevil = m+1,l+1
#             crr.append(list(onevil))
#             seto.add(onevil)
#     for n in range((x-k+1)**2):
#         if k == 0:
#             break
#         if len(seto) == len(crr) + len(brr):
#             count+=1
#             crr.clear()
#             seto = grr.copy()
#             break
#         elif len(seto) != len(crr) + len(brr):
#             seto = grr.copy()
#             for o in crr:
#                 o[1]+=1
#                 seto.add(tuple(o))
#                 if [k+counter,x] == o:
#                     seto = grr.copy()
#                     counter+=1
#                     for q in crr:
#                         q[1]-=(x-k)
#                         q[0]+=1
#                         seto.add(tuple(q))
#         counter = 0
        
# print(count)
x = int(input())
y = input()
z = list(map(int, input().split()))
print(min(x-min(z[0],z[1]))

                            
            
                        
            
        
