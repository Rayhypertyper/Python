x = int(input())
my_dict = dict()
bigrest = []
intrest = []
smolrest = []
for i in range(x):
    y = list(map(int, input().split()))
    a = f"{y[0]*100} {y[1]*100}"
    smolrest.append(y)
    intrest.append(y)
    intrest[i][0]*=100
    intrest[i][1]*=100
    my_dict[a] = 0
for i in range(1001):
    for j in range(1001):
        min_dis = float('inf')
        for k in intrest:    
            if ((i-k[0])**2 + (j-k[1])**2) < min_dis:
                min_dis = ((i-k[0])**2 + (j-k[1])**2)
                b = f"{k[0]} {k[1]}"
        my_dict[b]+=1
for i in my_dict:
    c = list(map(int, i.split()))
    c[0]/=1000000
    round(c[0])
    c[1]/=1000000
    round(c[1])
    print(f"Restaurant at ({int(c[0])},{int(c[1])}) serves {my_dict[i]}% of the population")

#   for i in range(x):
#     y = input()
#     arr.append(list(map(int, y.split())))
#     brr.append(list(map(int, y.split())))
#     arr[i][0]*=10
#     arr[i][1]*=10
#     d = f"{arr[i][0]} {arr[i][1]}"
#     my_dict[d] = 0
# n = input()
# for j in range(1,101):
#     for k in range(1,101):
#         distance = float('inf')
#         closest = ''
#         for l in arr:
#             if (((j-l[0])**2)+((k-l[1])**2))**(1/2) < distance:
#                 b = f"{l[0]} {l[1]}"
#                 distance = (((j-l[0])**2)+((k-l[1])**2))**(1/2)
#         my_dict[b]+=1
# for i in my_dict:
#     my_dict[i]/=100
#     my_dict[i] = int(round(my_dict[i]))
#     crr = list(map(int, i.split()))
#     print(f"Restaurant at ({int(crr[0]/10)},{int(crr[1]/10)}) serves {my_dict[i]}% of the population.")

# for j in range(1,10):
#     for k in range(1,10):
#         distance = float('inf')
#         closest = ''
#         for l in arr:
#             print(str((l[0]-k)**2), str((l[1]-j)**2 ))
#             if (l[0]-k)**2 + (l[1]-j)**2 < distance:
#                 a = str(l[0])
#                 b = str(l[1])
#                 c = f"{a} {b}"
#                 closest = c
#                 distance = (l[0]-k)**2 + (l[1]-j)**2
#         my_dict[closest]+=1
# for i in my_dict:
#     print(f"Restaurant at ({i[0]},{i[2]}) serves {my_dict[i]}% of the population")

