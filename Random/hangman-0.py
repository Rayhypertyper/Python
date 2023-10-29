import requests
from random import randint
from os import system

word_list = []
with open("words.txt", "r") as r_file:
    word_list = r_file.readlines


import requests         
from random import randint
from os import system


user_word = []
wrong = 0

def output_hangman(wrong):
    if (wrong == 0):
        pass
    if (wrong == 1): 
        print("   _____ \n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 2): 
        print("   _____ \n"
            "  |     | \n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 3): 
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 4): 
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n")

def output_word():
    for chr in user_word:
        print(chr, end=" ")

word_list = []
with open("words.txt", "r") as r_file:
    word_list = r_file.readlines()         

word = word_list[randint(0, len(word_list)-1)]
min_length = 5
while (len(word) < min_length):
    word = word_list[randint(0, len(word_list)-1)]

system("cls")
word = word.strip()


for i in range(len(word)):
    user_word.append("_")


while (user_word.count("_") > 4):
    prepare_chr = chr(96 + randint(1, 26))
    for i in range(len(word)):
        if (prepare_chr == word[i]):
            user_word[i] = prepare_chr

for i in range(4):
    if "_" in user_word:
        if (wrong < 4):
            system("cls")
            print("Let's play Hangman game!")
            print("This word has total {} letters.".format(len(word)))
            print(word)
            output_hangman(wrong)   # Use the wrong for output hangman
            output_word()
            chr_input = input("\n\nInput the char: ")
            not_match = False
            for i in range(len(word)):
                if (chr_input == word[i]):
                    user_word[i] = chr_input
                    not_match = True
            if not not_match:
                wrong += 1
        else:
            
            system("cls")
            output_hangman(wrong)
            output_word()
            print("\n You lost!")
            print("The word is", word)
            exit()
    else:
        
        print()
        output_word()
        print("\nYou won!")

if (wrong < 5):
    
    system("cls")
    output_word()
    print("\n You Win!")
else:
   
    system("cls")
    output_hangman(wrong)
    print("\n You lost!")
    print("The word is", word)


