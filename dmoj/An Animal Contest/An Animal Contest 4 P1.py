x = list(map(int, input().split()))
y = list(input())
z = list(map(int, input().split()))
# arr = []
# for i in range(len(z)):
#     arr.append(i+1)
# for j in range(z[-1]):
#     for k in range(len(y)):
#         if y[k] == '0':
#             arr
for i in range(len(z)-1):
    y.pop(-1-i)
    if y[i] == z[-1] and y[i] == '0':
        y+=y[0:z[-1]]
        del y[:z[-1]]
        break
    elif y[i] == '0':
        y.pop(i)
print(*y, sep='')

    