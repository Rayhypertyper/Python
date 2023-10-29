import tkinter as tk
from tkinter import *
from tkinter import filedialog , Text
import os
import random
import numpy as np
from tkinter import *
from tkinter.ttk import *
import pyperclip

 


root = Tk()
root.geometry("200x200")

deej = "hi"
word = "banana"
wordstorage = []
lengtha = len(word)
a = 0

c = 0
output = ''
for x in range (lengtha):
    wordstorage.append(word[a])
    a+=1
    
random.shuffle(wordstorage)
wordstorage2 = np.block(wordstorage)
def random():
    print("hi")
    # b = 0
    # for y in wordstorage2:
    #     print(wordstorage2[b], end='')
    #     b+=1






def play():
    newWindow = Toplevel(root)
    newWindow.title("Game")
    newWindow.geometry("200x200")
    Label(newWindow, text ="Your word is ").pack()
    Label(command=random).pack()
label = Label(root, text ="Welcome to Unscremble\nClick below to get started").pack()


myButton = Button(root, text="Play", command=random)
myButton.grid(row=0, column=0, columnspan=2, pady=10)
exitButton = Button(root, text="Exit", command=root.quit)
exitButton.pack()
mainloop()

 
# myButton = Button(root, text="Play",  command=play)
# myButton.pack()
# exitButton = Button(root, text="Exit", padx=101, pady=22, command=root.quit)
# exitButton.pack()

root.mainloop()