import pyautogui
import math
import time

# Radius 
R = 400
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
screen_width, screen_height = pyautogui.size()
X = screen_width // 2
Y = screen_height // 2
# offsetting by radius 5
pyautogui.dragTo(X+R,Y)

for i in range(450):
    # setting pace with a modulus 
    if i%15==0:
       pyautogui.dragTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))