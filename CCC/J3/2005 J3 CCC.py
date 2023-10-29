
import math 
x = input()
arr = []
arr.append(x)
while x != "SCHOOL":
    x = input()
    arr.append(x)
arr.reverse()
for i in range(len(arr)):
    if arr[i] == 'L':
        arr[i] = 'RIGHT'
    elif arr[i] == 'R':
        arr[i] = 'LEFT'
for i in range(math.ceil(len(arr)/2)):
    try:
        print(f"Turn {arr[(i+1)*2-1]} onto {arr[(i+1)*2]} street.")
    except:
        print(f"Turn {arr[-1]} into your HOME.")
    
