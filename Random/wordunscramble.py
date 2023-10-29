
import random
import numpy as np
word = "banana"
wordstorage = []
lengtha = len(word)
a = 0
b = 0
c = 0
output = ''

print('Welcome to word unscramble, to get started type start, and to exit type quit')
x = input()
while x == 'start':
    break

while x == 'quit':
    exit

    
   

for x in range (lengtha):
    wordstorage.append(word[a])
    a+=1


random.shuffle(wordstorage)
wordstorage2 = np.block(wordstorage)


print("Your scrambled word is: ")
for y in range (lengtha):
    print(wordstorage2[b], end='')
    b+=1

userinput = input("\nEnter your guesses down here\n")
if userinput == 'banana':
        print("Correct")
        exit
        
while userinput != 'banana':
    if userinput != 'banana':
        print("Wrong")
        userinput = input("Please try again\n")
        
    if userinput == 'banana':
        print("Correct")
        break


    

