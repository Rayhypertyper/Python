# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)
# print(factorial(5))

def sumnum(y):
    if y == 1:
        return y
    else:
        return y + sumnum(y-1)
print(sumnum(5))
#____________________________
x = int(input())
def fib(depth,a,b,x):
    if x == 0:
        return
    if x == 1:
        print(1)
        return
    c = b
    b = a+b
    a = c
    print(a)
    if x == depth+1:
        return
    fib(depth+1,a,b,x)
fib(0,0,1,x)
    