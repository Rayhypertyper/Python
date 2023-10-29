import random

x = ["rock", "paper", "scissor"]
robot = random.choice(x)

user = input("Please choose rock, paper, or scissors")
if user == 'rock'.lower() and robot == 'rock':
  print('Tie')
elif user == 'rock'.lower() and robot == 'paper':
  print('You lost.')
elif user == 'rock'.lower() and robot == 'scissors':
  print('You won!')
elif user == 'paper'.lower() and robot == 'rock':
  print('You won!')
elif user == 'paper'.lower() and robot == 'paper':
  print('Tie')
elif user == 'paper'.lower() and robot == 'scissors':
  print('You lost.')
elif user == 'scissors'.lower() and robot == 'rock':
  print('You lost.')
elif user == 'scissors'.lower() and robot == 'paper':
  print('You won!')
elif user == 'scissors'.lower() and robot == 'scissors':
  print('Tie')