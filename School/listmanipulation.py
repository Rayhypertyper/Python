import sys

def inpval(x,a):
  while True:
      if x.isdigit():  
        if 0<int(x)<=a:
            x = int(x)
            return x
      x = input("Please enter a number within the range of the list\n")
            

def yn(y):
    while y != 'y' and y != 'n':
        y = input("Invalid input! To add a value, enter y, else, enter n\n")
    return y

def space(x):
    while x.isspace() or x == '':
        x = input()
    return x

list = []
print("list is empty")
while True:
    x = input('Please add a value to the list\n')
    space(x)
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
    x = inpval(input("Please enter the number corresponding to the element you want to change\n"),len(list))
    y = input("Enter what you want this value corresponding to the number to be changed into\n")
    space(y)
    list[x-1] = y
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    y = input("To change another a value, enter y, else, enter n\n")
    yn(y)
    if y == 'y':
        continue
    if y == 'n':
        break

while True:
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    x = inpval(input("Please enter the number corresponding to the element you want to delete\n"),len(list))
    list.pop(x-1)
    if not list:
        print("The list is empty. Goodbye!")
        sys.exit()
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    y = input("To delete another value, enter y, else, enter n\n")
    yn(y)
    if y == 'y':
        continue
    if y == 'n':
        break
print("Goodbye!")



    