import random
import numpy as np
message = ""

arr = []
print("Welcome to word scrambler\nTo end, type quit\nTo start type in the word you want")
message = input()
lengtha = len(message)

while message != 'quit':
    x = 0
    b = 0
    for a in range (lengtha):
        arr.append(message[x])
        x+=1

    random.shuffle(arr)
    wordstorage2 = np.block(arr)
    print("The scrambled version of " + message + " is:")
    for y in range (lengtha):
        print(wordstorage2[b], end='')
        b+=1
    print("\n")
    print("Enter a new word here:")
    message = input()
    arr.clear()
    lengtha = len(message)
    
    

        




    





