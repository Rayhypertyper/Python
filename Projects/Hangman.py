# from Words import words
print('Welcome to hangman :)')
print()
while True:    
    from Words import words, my_dict
    import random
    import time
    import sys
    word = random.choice(words)
    arr = []
    lives = 0
    brr = ['_']*len(word)
    while True:
        x = input("Your guess is: ")    
        if len(x) != 1 or not x.isalpha():
            print("PLEASE ENTER A VALID INPUT")
            continue
        arr.append(x)
        if x in word:
            print(my_dict[lives])
            for i in range(len(word)):
                if x == word[i]:
                    brr[i] = x
            time.sleep(1)
            print(' '.join(map(str, brr)))
            print('You have used the chracters', ' '.join(map(str, arr)))
            print()
            time.sleep(1)
            if brr == list(word):
                print("YOU WON GOOD JOB with the word: " + word)
                print()
                print("TO PLAY AGAIN PRESS p AND TO QUIT PRESS q")
                y = input()
                if y == 'q':
                    sys.exit()
                elif y == 'p':
                    break
                break
                
        else:
            lives+=1
            print(my_dict[lives])
            time.sleep(1)
            print(' '.join(map(str, brr)))
            time.sleep(1)
            if lives == 6:
                print()
                print("THE WORD WAS " + word)
                print()
                print("HANGMAN")
                print()
                print("TO PLAY AGAIN PRESS p AND TO QUIT PRESS q")
                y = input()
                if y == 'q':
                    sys.exit()
                elif y == 'p':
                    break
            print('You have used the chracters', ' '.join(map(str, arr)))
            print()
            

            
            

