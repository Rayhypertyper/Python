import random
import sys
import os
import time
#code to make a dictionary
# dict = {}
# for i in range(40):
#     x = input()
#     y = input()
#     dict[x] = y
# print(dict)

#dict of what i need
dict = {'H': 'hydrogen', 'Cr': 'chromium', 'He': 'helium', 'Mn': 'manganese', 'Li': 'lithium', 'Fe': 'iron', 'Be': 'beryllium', 'Co': 'cobalt', 'B': 'boron', 'Ni': 'nickel', 'C': 'carbon', 'Cu': 'copper', 'N': 'nitrogen', 'Zn': 'zinc', 'O': 'oxygen', 'As': 'arsenic', 'F': 'fluorine', 'Br': 'bromine', 'Ne': 'neon', 'Ag': 'silver', 'Na': 'sodium', 'Cd': 'cadmium', 'Mg': 'magnesium', 'Sn': 'tin', 'Al': 'aluminium', 'Sb': 'antimony', 'Si': 'silicium', 'I': 'iodine', 'P': 'phosphorous', 'Sr': 'strontium', 'S': 'sulphur', 'Ba': 'barium', 'Cl': 'chlorine', 'Au': 'gold', 'Ar': 'argon', 'Hg': 'mercury', 'K': 'potassium', 'Pb': 'lead', 'Ca': 'calcium', 'U': 'uranium'}

print("Welcome to element to symbol and vice versaer. This is to help you ace the quiz for SNC2DE test. ")
while True:
    boo = False
    x = input("1. Get quizzed on symbols\n2. Get quizzed on elements\n3. Exit\nInput: ")
    if x == '1':
        a = random.choice(list(dict.keys()))
        for i in range(3):
            y = input(f"What element is {a}\n")
            y = y.lower()
            if dict[a] == y:
                print("Correct!")
                time.sleep(1)
                boo = True
                break
            else:
                print("Incorrect.")
        if not boo:
            os.system('cls')
            print(f"The element is for {a} is {dict[a]}")
            time.sleep(2)
    elif x == '2':
        a = random.choice(list(dict.values()))
        for i in range(3):
            y = input(f"What is the chemical symbol for {a}\n")
            y = y.capitalize()
            try:
                if dict[y] == a:
                    print("Correct!")
                    time.sleep(1)
                    boo = True
                    break
                else:
                    print("Incorrect.")
            except:
                print("Incorrect.")
        if not boo:
            os.system('cls')
            t = list(dict.keys())
            v = list(dict.values())
            position = v.index(a)
            g = t[position]
            print(f"The chemical symbol for {a} is {g}")
            time.sleep(2)
    else:
        sys.exit()
    os.system('cls')