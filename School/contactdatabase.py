import os

print("ICS3U Summative 1: Simple Contacts Database")

def ispace(x):
  while x.isspace() or x == '':
    x = input('Invalid input! Please input a nonspace value!\n')
  return x

def phoneval(a,contacts,boo,inp):
  global b
  b = inp
  if b == '' and boo == 'n':
        b = contacts[int(a)-1][2]
        return b
  while not b.isdigit() or len(b) != 10:
    b = input("To replace the existing phone number, please enter a 10 numberic chracter phone number with no spaces, brackets or hyphens!\n")
    if b == '' and boo == 'n':
        b = contacts[int(a)-1][2]
        return b
  b = f"({b[0:3]}) {b[3:6]}-{b[6:11]}"
  return b

def enter(c,type,index, contacts):
  a = input(f"Please enter a {type} to replace {contacts[int(c)-1][index]}. To keep {contacts[int(c)-1][index]}, press enter\n")
  if index == 2:
    a = phoneval(c,contacts,'n',a)  
    contacts[int(c)-1][index] = a

def inputval(x, contacts, num):
  while True:
    if x.isdigit():
      if num == 7:
        if 0 < int(x) < 7: 
          return x
      elif num == 1:
        if x == '1' or x == '6':
          return x
      else:
        if 0 < int(x) <= len(contacts): 
          return x
    x = input("Please enter a number within the range of the list\n")

def msg(x, contacts):
  os.system('clear')
  print(f'The {x}!')
  if x == 'contact was successfully deleted' and contacts == []:
    print("They contacts list is empty!")
    start()
  options(contacts)

def ynval(g):
  while g not in ['n','y']:
    g = input("Invalid input! y = yes, n = no\n")
  return g

def start():
  print('1. Enter a contact \n6. Exit program')
  contacts = []
  a = inputval(input(), contacts, 1)
  if a == '1':
    add(contacts)
  elif a == '6':
    print("Thank you for playing! Goodbye!")
    return 

def add(contacts):
  os.system('clear')
  fname = ispace(input('Please enter your first name\n'))
  lname = ispace(input('Please enter you last name\n'))
  phone = phoneval(':)',contacts,'y',input("Please enter your phone number\n"))
  contacts.append([fname,lname, phone])
  msg('contact was successfully added', contacts)

def edit(contacts):
  os.system('clear')
  display(contacts)
  c = inputval(input('Please enter number beside the value you want to edit\n'), contacts, len(contacts))
  enter(c,'first name', 0, contacts)
  enter(c,'last name', 1, contacts)
  enter(c,'phone number', 2, contacts)
  msg('contact was successfully edited', contacts)

def delete(contacts):
  os.system('clear')
  display(contacts)
  c = inputval(input('Please enter number beside the value you want to delete\n'), contacts, len(contacts))
  contacts.pop(int(c)-1)
  msg('contact was successfully deleted', contacts)
  if contacts == []:
    start()

def display(contacts):
  os.system('clear')
  print(f"{'#':<4}{'First Name':<13}{'Last Name':<12}{'Phone Number'}")
  for i in range(len(contacts)):
    print(f"{(str(i+1)+'.'):<4}{contacts[i][0]:<13}{contacts[i][1]:<12}{contacts [i][2]}")

def delall(contacts):
  os.system('clear')
  a = ynval(input("Do you confirm to deleting all values in the contacts? (y/n)\n"))
  if a == 'y':
    contacts.clear()
    os.system('clear')
    print("The contacts is empty!")
    start()
  elif a == 'n':
    os.system("clear")
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
  elif a == '6':
    os.system('clear')
    print("Thank you for playing! Goodbye!")
    return

start()