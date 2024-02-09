x = int(input())
arr = []
my_dict = {}
for i in range(x):
    y = list(map(int, input().split()))
    my_dict[i+1] = y[1:] 
visited = {1}
minum = 99999999
def find(depth,num,setnum):
    global visited, minum
    if setnum == []:
        if depth < minum:
            minum = depth
        depth-=1
        return
    for j in setnum:
        if j in visited:
            depth-=1
            return
        visited.add(j)
        find(depth+1,i,my_dict[j])
    if len(visited) == x:
        return "Y",minum
    else:
        return "N",minum
x = find(1,0,my_dict[1])
print(x[0])
print(x[1])











# visited = []
# seto = set()
# def find(depth,a,b):
#     global seto,visited
#     seto.add(a)
#     for i in b:
#         if i in arr:
#             depth-=1
#             return
#         visited.append(i)
#         find(depth+1,i,my_dict[i])
        
#     if len(seto) == x:
#         return "y"
#     else:
#         return 'n'
# print(find(0,1,my_dict[1]))







# for i in range(len(my_dict)):
#     arr.append(i)
#     for j in my_dict[i+1]:
#         arr.append(j)
#         while True:
#             for k in my_dict[j]:
#                 arr.append(k)
#                 if k == x:
#                     pass
#                 else:
#                     pass


    
            
    

        
        
    
    



    