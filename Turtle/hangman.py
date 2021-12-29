import requests
import numpy as np   
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)
print(response.content)

WORDS = response.content.splitlines()
print(WORDS)
print(len(WORDS[5]))
print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "__|__\n")
