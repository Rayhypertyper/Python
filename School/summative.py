import os

print("ICS3U Summative 1: Simple Contacts Database")

def ispace(x):
  while x.isspace() or x == '':
    x = input('Invalid input! Please input a nonspace value!\n')
  return x

def phoneval(a):
  while not a.isdigit() or len(a) != 10:
    a = input("Please enter a 10 numberic chracter phone number with no spaces, brackets or hyphens!\n")
  return a

def inputval(x, contacts, num):
  while True:
    if x.isdigit():
      if num == 7:
        if 0 < int(x) < 7: 
          return x
      else:
        if 0 < int(x) <= len(contacts): 
          return x
    x = input("Please enter a number within the range of the list\n")

def enter(c,type,index, contacts):
  a = input(f"please enter a {type} to replace {contacts[int(c)-1][index]}. To keep {contacts[int(c)-1][index]}, press enter\n")
  if a == '':
    return
  else:
    if index == 2:
      a = phoneval(a)
    contacts[int(c)-1][index] = a


def start():
  print('1. Enter a contact')
  print('6. Exit program')
  contacts = []
  a = input()
  if a == '1':
    add(contacts)
  elif a == '6':
    print("Thank you for playing! Goodbye!")
    return 
    
def add(contacts):
  os.system('cls')
  fname = ispace(input('please enter your first name\n'))
  lname = ispace(input('please enter you last name\n'))
  phone = phoneval(input("please enter your phone number\n"))
  contacts.append([fname,lname, phone])
  os.system('cls')
  print('The contact was succesfully loaded')
  options(contacts)

def edit(contacts):
  os.system('cls')
  display(contacts)
  c = inputval(input('Please enter number beside the value you want to edit\n'), contacts, len(contacts))
  enter(c,'first name', 0, contacts)
  enter(c,'last name', 1, contacts)
  enter(c,'phone number', 2, contacts)
  os.system('cls')
  print('The list was successfully updated')
  options(contacts)
  
def delete(contacts):
  os.system('cls')
  display(contacts)
  c = inputval(input('Please enter number beside the value you want to delete\n'), contacts, len(contacts))
  contacts.pop(int(c)-1)
  print("Contacts successfully deleted") #the delete word can be fstringed and changed if put back into the enter func
  if contacts == []:
    pass #problem with instructions here
  options(contacts)

def display(contacts):
  print("# First Name Last Name Phone Number")
  for i in range(len(contacts)):
    print(f"{i+1}. {contacts[i][0]} {contacts[i][1]} {contacts [i][2]}")

def delall(contacts):
  os.system('cls')
  g = input("do you confirm to deleting all values in the contacts (y/n)\n")
  if g == 'y':
    contacts = []
    os.system('cls')
    print('The database is empty!')
    options(contacts)
  elif g == 'n':
    os.system('cls')
    options(contacts)
  
def options(contacts):
  a = inputval(input("1. Add a Contact\n2. Edit a Contact\n3. Delete a Contact\n4. Delete all Contacts\n5. Display Contacts\n6. Exit Program\n"), contacts, 7)
  if a == '1':
    add(contacts)
  elif a == '2':
    edit(contacts)
  elif a == '3':
    delete(contacts)
  elif a == '4':
    delall(contacts)
  elif a == '5':
    display(contacts)
  elif a == 6:
    os.system('cls')
    print("Thank you for playing! Goodbye!")
    return 

start()

#DONT FORGET TO CHANGE BACK INTO CLEAR NOT CLSus
  