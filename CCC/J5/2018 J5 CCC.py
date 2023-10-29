x = int(input())
arr = []
my_dict = {}
for i in range(x):
    y = list(map(int, input().split()))
    my_dict[i+1] = y[1:] 
print(my_dict)
for i in range(len(my_dict)):
    arr.append(i)
    for j in my_dict[i+1]:
        arr.append(j)
        while True:
            for k in my_dict[j]:
                arr.append(k)
                if k == x:
                    pass
                else:
                    pass
                    

    
            
    

        
        
    
    



    