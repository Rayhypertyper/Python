import math
a = int(input())
b = int(input())
c = int(input())

try:
    d = b**2-(4*a*c)
    sum =math.sqrt(d)
    dim = (-b + sum) / (2*a)
    sim = (-b - sum) / (2*a)
    print(dim)
    print(sim)
except:
    print(-b, end=' + ')
    print(b**2-(4*a*c))
    print('---------')
    print(2*a)
    print('')
    print(-b, end=' - ')
    print(b**2-(4*a*c))
    print('---------')
    print(2*a)