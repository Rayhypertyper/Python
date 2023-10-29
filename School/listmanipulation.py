import sys

def inpval(x,a):
    while True:    
        try:
            x = int(input("Please enter a number within the range of the list"))
            if x>=a and x<=0:
                x = input("Please enter a number within the range of the list")
        except:
            x = int(input("Please enter a number within the range of the list"))
    return int(x)

def yn(y):
    while y != 'y' and y != 'n':
        y = input("Invalid input! To add a value, enter y, else, enter n\n")
    return y

list = []
print("list is empty")
while True:
    x = input('Please add a value to the list\n')
    while x.isspace() or x == '':
        x = input()
    list.append(x)
    print("The list:")
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    y = input("To add a value, enter y, else, enter n\n")
    yn(y)
    if y == 'y':
        continue
    if y == 'n':
        break
    
while True:
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    x = input("Please enter the number corresponding to the element you want to change\n")
    a = len(list)
    h = inpval(x,a)
    list[x-1] = h
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    y = input("To edit another value, enter y, else, enter n\n")
    yn(y)
    if y == 'y':
        continue
    if y == 'n':
        break

while True:
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    x = input("Please enter the number corresponding to the element you want to change\n")
    a = len(list)
    inpval(x,a)
    list.pop(x-1)
    if not list:
        print("The list is empty. Goodbye!")
        sys.exit()
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    y = input("To edit another value, enter y, else, enter n\n")
    yn(y)
    if y == 'y':
        continue
    if y == 'n':
        break
print("Goodbye!")



    