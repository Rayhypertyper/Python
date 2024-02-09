from unidecode import unidecode
# lowercaselizer
#this is necessary cuz the next program can't take capitales
# x = input()
# arr = []
# while x != '0':
#     arr.append(x)
#     x = input()
# for i in arr:
#     print(i.lower())

#press 0 to terminate program to print results

#character width calculator
#had to measure each one out
#gotta use this one before capitalizer and make sure none is capitlalized
#unidecode is so accents count as regular words just for calcsa
letterlen = {"a": 13, "b": 15, "c": 11.75, "d": 15, "e": 13.5, "f": 8, "g": 13, "h": 14.5, "i": 6.25, "j": 6.25, "k": 12.75, "l":6.25, "m":22, "n": 14.5, "o": 15, "p": 15, "q": 15, "r":8.75, "s":11, "t":8.5, "u":14.5, "v":12.25, "w":18.25, "x":11.75, "y":12.5, "z":11.75}
x = 1
mydict = {}
x = input()
while x !='0':
    counter = 0
    for i in range(len(x)):
            if x[i] != ':':
                a = x[i].lower()
                counter+=letterlen[unidecode(a)]
            else:
                break
    mydict[counter] = x
    x = input()
sortedict = dict(sorted(mydict.items()))
for key, values in sortedict.items():
    print(values.capitalize())

    