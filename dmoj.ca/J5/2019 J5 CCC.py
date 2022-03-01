x = int(input())
arr = []
flag = True
for i in range(x):
    y = int(input())
    a = (y-2)/2
    try:
        for j in range(int(a)):
            arr.append(y-(j+2))
            arr.append(y-(y-(j+2)))
    except:
        pass
    for k in range(len(arr)):
        for l in range(2, len(arr)):
            if (int(arr[k]) % l) == 0:
                k+=2
            else:
                if int(arr[k+1] % 1) == 0:
                    

                
            
            
           

                

