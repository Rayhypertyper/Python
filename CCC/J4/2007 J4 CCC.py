x = list(input())
y = [i for i in x if i != ' ']
a = list(input())
b = [k for k in a if k != ' ']
y.sort()
b.sort()
if b == y:
    print("Is an anagram.")
elif b != y:
    print("Is not an anagram.")