# x = int(input())
# i = 0
# a = 0
# b = 0
# c = 0
# if x%4 == 0 or x%5 == 0:
#     print(int(x/20)+1)
# else:
#     for i in range(4):
#         b = int((x/4)-(i+1))
#         c = int(5*(i+1))
#         d = c/5
#         if x == 4*b+c:
#             break
            
#     if int(b/4)+int(d/5) == 0:
#         print(0)
#     elif int(int(b/4)+int(d/5)) > 0:
#         print(int(int(b/4)+int(d/5)+1))
   
x = int(input())
count = 0
a = 0
for i in range(50000000000):
    if (x-(x-5*i))%4 == 0:
        count+=1
    if x-5*i <= 0:
        break 
    
print(count)
    

    
