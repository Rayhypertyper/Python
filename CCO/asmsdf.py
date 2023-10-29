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
