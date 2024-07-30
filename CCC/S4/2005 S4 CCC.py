# def dfs(value, depth):
#   global l, dict
#   try:
#       for i in dict[value]:
#           dfs(i, depth+1)
#           if dict[value].index(i) + 1 == len(dict[value]):
#               if value == 'Home':
#                   return l*20
#               depth-=1
#               return
#   except:
#     l = max(l, depth)
#     depth-=1
#     return
# x = int(input())
# for i in range(x):
#   dict = {}
#   l = 0
#   y = int(input())
#   for i in range(int(y/2)):
#       a = input()
#       b = input()
#       if b != "Home":
#           if a not in dict:
#               dict[a] = [b]
#           else:
#               dict[a].append(b)
#       else:
#           if b not in dict:
#               dict[b] = [a]
#           else:
#               dict[b].append(a)
#   dfs("Home", 0)
#   print(l*20)

#new solution
arr = [] #all the names
brr = [] #nodes at the bottom of tree
crr = [] #the nodes right after home
drr = []
def indt(b, arr, crr, depth):
    b = arr.index(arr[b-1])
    if arr[b] in crr:
        return depth
    return indt(b, arr, crr, depth+1)
    
x = int(input())
for i in range(x):
    y = int(input())
    for j in range(y):
        z = input()
        arr.append(z)
    #finds all the ones at botom of the tree cuz they are sandwiched by 2 of the same ones 
    for i in range(len(arr)):
        if i != 0 and i!=len(arr)-1:
            if arr[i-1] == arr[i+1]:
                brr.append(arr[i])
    #finds all the ones right off from home so we know when to stop
        if i!=len(arr)-1:
            if arr[i+1] == "Home":
                crr.append(arr[i])      
    for i in brr:
        a = arr.index(i)
        l = 0
        a = indt(a, arr, crr, 1)
        l = max(l, a)
    print(l*20)
        
