import keyboard
from time import sleep
sleep(1)
number = 2
while True:
    keyboard.write(str(number))
    number = 2 + number
    keyboard.wait("enter")