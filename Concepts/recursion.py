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

def listperm(x):
    