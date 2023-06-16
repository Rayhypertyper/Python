# import pyautogui
# # https://www.virtualmusicalinstruments.com/xylophone
# pyautogui.moveTo(330, 351) #middle c
# pyautogui.click() 
# pyautogui.moveTo(290, 351) #left b
# pyautogui.click() 
# pyautogui.moveTo(250, 351) #left a
# pyautogui.click() 
# pyautogui.moveTo(210, 351) #left g
# pyautogui.click() 
# pyautogui.moveTo(210, 351) #left g
# pyautogui.click() 
# pyautogui.moveTo(250, 351) #left a
# pyautogui.click() 
# pyautogui.moveTo(330, 351) #middle c
# pyautogui.click() 
# pyautogui.moveTo(60, 351) #left c
# pyautogui.click() 
# arr = ['1','a','b']
# brr = ['1','b','b']
# for i in arr:
#     for j in brr:
#         r = all(elem in i for elem in j)
#         if not r:
#             print(r)
# x = bool(1)
# if x:
#     print('yes')
# arr = ['1', '2', 'a']
# a = arr.pop(0)
# print(a)
def factorial(x):


    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
print(factorial(int(input())))