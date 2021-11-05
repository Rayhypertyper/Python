import requests 
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)
# print(response.text)
WORDS = response.text.splitlines()   # data type of WORDS is list (string array)
print(WORDS)

with open("words.txt", "w") as w_file:
    for word in WORDS:
        w_file.write(word + '\n')
    