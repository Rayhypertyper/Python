# import time
# st = time.time()
# for i in range(1000):
#     print(i)
#     print('hello world')
# en = time.time()
# print(en-st)

# import sys

# s1 = input()
# s2 = input()

# #first solution
# if s1 in s2:
#     print("y")
# else:
#     print('n')

# #second solution
# for i in range(len(s2)-len(s1)+1):
#     if s1 == s2[i:i+len(s1)]:
#         print('y')
#         sys.exit()
# print('n')
# s1 = input()

# vowel = ['a','e','i','o','u']
# vowelc = 0
# consonant = 0
# for i in s1:
#     if i in vowel:
#         vowelc+=1
#     elif i not in vowel and i.isalpha():
#         consonant+=1
# print(f"v: {vowelc}, c:{consonant}")

i = list(input())
elist = []
olist = []
for a in range(len(i)):
    if a%2 == 0:
        olist.append(i[a])
    elif a%2 == 1:
        elist.append(i[a])
elist.sort(reverse=True)
olist.sort(reverse=True)
b = ''.join(map(str, elist))
c = ''.join(map(str,olist))
print(int(b)+int(c))


