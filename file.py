import requests 
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)
print(response.content)# print(response.content)