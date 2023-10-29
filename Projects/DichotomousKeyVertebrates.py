import os

def inpval(x,y):
  if y == 'fur':
    while x != '1' and x != '2' and x !='b' and x!='s' and x!='e':
      x = input(f"Invalid input! Please enter 1 if it has {y} and 2 if it doesn't have {y}.\n") 
  else:
    while x != '1' and x != '2' and x !='b' and x!='s' and x!='e':
      x = input(f"Invalid input! Please enter 1 if it has {y} and 2 if it doesn't have {y}. {back()}\n")
  return x

def back():
  return "If you want to go back one step, please enter b. If you want to start over again, please enter s. To terminate the program, please enter e."

def backuv(x):
  while x !='b' and x!='s' and x!='e':
      x = input(f"Invalid input! {back()}\n")
  return x
  
def firststep():
  os.system('clear')
  print("Welcome to Vertebrate recongizer")
  y = 'fur'
  x = input(f"Does it have {y} or not? If it has {y} enter 1, if it doesn't have {y} enter 2. {back()}\n")
  x = inpval(x,y)
  if x == '1':
    mammal()
  elif x == '2':
    secondstep()
  elif x == 'e':
    return
def mammal():
  os.system('clear')
  print("It is a mammal.")
  print(back())
  x = input()
  backuv(x)
  if x == 'b' or x == 's':
    firststep()
  elif x == 'e':
    return

def secondstep():
  os.system('clear')
  y = 'feathers'
  x = input(f"Does it have {y} or not? If it has {y} enter 1, if it doesn't have {y} enter 2. {back()}\n")
  x = inpval(x,y)
  if x == '1':
    feathers()
  elif x == '2':
    thirdstep()
  elif x == 'b' or x == 's':
    firststep()
  elif x == 'e':
    return

def feathers():
  os.system('clear')
  print('It is a bird.')
  print(back())
  x = input()
  backuv(x)
  if x == 'b':
    secondstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return

def thirdstep():
  os.system('clear')
  y = 'dry skin'
  x = input(f"Does it have {y} or not? If it has {y} enter 1, if it doesn't have {y} enter 2. {back()}\n")
  x = inpval(x,y)
  if x == '1':
    dryskin()
  elif x == '2':
    fourthstep()
  elif x == 'b':
    secondstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return

def dryskin():
  os.system('clear')
  print("Reptile")
  print(back())
  x = input()
  backuv(x)
  if x == 'b':
    thirdstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return

def fourthstep():
  os.system('clear')
  y = 'scales'
  x = input(f"Does it have {y} or not? If it has {y} enter 1, if it doesn't have {y} enter 2. {back()}\n")
  x = inpval(x,y)
  if x == '1':
    amphibian()
  elif x == '2':
    fish()
  elif x == 'b':
    thirdstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return

def amphibian():
  os.system('clear')
  print("It is an amphibian.")
  print(back())
  x = input()
  backuv(x)
  if x == 'b':
    fourthstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return
    
def fish():
  os.system('clear')
  print("It is an fish.")
  print(back())
  x = input()
  backuv(x)
  if x == 'b':
    fourthstep()
  elif x == 's':
    firststep()
  elif x == 'e':
    return
firststep()
print("Thank you for playing vertebrate dichotomous key")