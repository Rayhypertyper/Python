# import numpy as np    
# x = ["a","b","c","d"]
# y = np.stack(x)
# print(y)
# for i in range(11): 
#     print(i, end=' ') 
# userinput = input("\nEnter your guesses down here\n")
import tkinter as tk
from tkinter import *
from tkinter import filedialog , Text
import os
import random
import numpy as np




root = Tk()
# output1= Label(root,text="Welcome to my game!\n ").grid(row=0, column=0)
# output2= Label(root,text="In this game, you will try to unscramble the given word\n").grid(row=1, column=0)
# output3 = Label(root,text="Here is your word:").grid(row=2, column=0)
# myButton = Button(root, text="Play", state=DISABLED, padx=100, pady=20)
# root.title("Unscramble")
# root.iconbitmap('C:/Users/Kai/Pictures/Screenshots')
# e = Entry(root, width=50, bg="blue", fg="white", borderwidth="2")
# e.pack()
# e.get()
# e.insert(0, "Enter Your Guess Here: ")
def myClick():
    myLabel = Label(root,text= "Wrong")
    myLabel.pack()

myButton = Button(root, text="Play", padx=100, pady=20, command=myClick)
myButton.pack()
exitButton = Button(root, text="Exit", padx=101, pady=22, command=root.quit)
exitButton.pack()



mainloop()