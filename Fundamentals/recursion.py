# #factorial
# def fact(a):
#     if a == 1:
#         return 1
#     return fact(a-1)*a
# print(fact(5))

#cacuates sum of first n natural nums
# def sum(a):
#     if a == 1:
#         return 1
#     return sum (a-1)+a

#recursive func to find power of num
def pow(a,b):
    if b == 0:
        return a
    return pow(a*a, b-1)
print(pow(2,2))

#rev a string
def rev(s):
    if len(s) == 1:
        return s
    return rev(s[1:]) + s[0]
print(rev("qwerty"))

#Write a function that calculates the value of the element on the kth cell of the nth row in Pascal’s Triangle (below) with recursion. Each element is equal to the sum of the two elements directly above it.
memo = {}

def count(r, c):
    if r == 0 and c == 0:
        return 1
    if c < 0 or c > r:
        return 0
    if (r, c) in memo:
        return memo[(r, c)]
    memo[(r, c)] = count(r - 1, c - 1) + count(r - 1, c)
    return memo[(r, c)]

print(count(100, 50))

#PROBLEM 2 CHALLENGE OF RECURSION SLIDES
values = [2, 4, 6, 7]
memo = {}

def coin(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x in memo:
        return memo[x]
    answer = False
    for value in values:
        if coin(x - value):
            answer = True
    memo[x] = answer
    return memo[x]

