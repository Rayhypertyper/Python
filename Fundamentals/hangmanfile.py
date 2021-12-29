import requests 
from random import randint
from os import system
# url = 'https://www.mit.edu/~ecprice/wordlist.10000'
# response = requests.get(url)
# # print(response.text)
# WORDS = response.text.splitlines()   # data type of WORDS is list (string array)
# print(WORDS)

# with open("words.txt", "w") as w_file:
#     for word in WORDS:
#         w_file.write(word + '\n')
with open("words.txt", "r") as r_file:
    word_list = r_file.readlines()
print(word_list)
random_int = randint(0, 9999)
word = word_list[random_int]
min_length = 8

while(len(word) < min_length):
    word = word_list[randint(0, 9999)]
print(word)
word = word.strip()
print(len(word))
print("this word has ", len(word), "letters")

word_storage = []
for i in range(len(word)):
    word_storage.append("_")
for i in range (len(word)):
    print('_', end = ' ')

print()
print("input your letter")