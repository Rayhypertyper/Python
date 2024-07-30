# a = int(input())
# b = int(input())
# if a == 0 or b == 0:
#     a = 0
#     b = 0
# print(a+b)

#q2
# x = int(input())
# arr = []
# counter = 0
# for i in range(x):
#     y = int(input())
#     arr.append(y)
#     arr.sort()
# arr.pop(-1)
# for i in range(len(arr)):
#     counter+=arr[i]
# print(int(counter/len(arr)))

#q3
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))
# bombs = 1
# streak = 1
# most = 1
# for i in range(len(y)-1):
#     if abs(y[i]-y[i+1]) <= x[1]:
#         streak+=1
#     else:
#         bombs+=1
#         most = max(most, streak)
#         streak = 1
# most = max(most, streak)
# print(bombs)
# print(most)

#q4
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(x[3]):
    if sum(y[:x[2]+1])

