# x = int(input())
# arr = []
# my_dict = {}
# for i in range(x):
#     y = list(map(int, input().split()))
#     my_dict[i+1] = y[1:] 
# visited = {1}
# minum = 99999999
# def find(depth,num,setnum):
#     global visited, minum
#     if setnum == []:
#         if depth < minum:
#             minum = depth
#         depth-=1
#         return
#     for j in setnum:
#         if j in visited:
#             depth-=1
#             return
#         visited.add(j)
#         find(depth+1,i,my_dict[j])
#     if len(visited) == x:
#         return "Y",minum
#     else:
#         return "N",minum
# x = find(1,0,my_dict[1])
# print(x[0])
# print(x[1])

#new solution
x = int(input())
dict = {}
l = 99999
boo = False
#sorts input into keys and values of a dictionary
for i in range(x):
    y = list(map(int, input().split()))
    dict[i+1] = y[1:]
seto = set()
# list to track the distance to each element
dist = [9999999 for i in range(10005)]
def search(value, depth):
    global seto, x, boo, dict, dist, l
    #checks if reaching this element has had a shorter path before. If it has, then goes back. This prevents infinite loops
    if dist[value] <= depth:
        depth-=1
        return
    #if there is a shorter path, then the list will update.
    dist[value] = depth
    #if we reach to an empty page, checks to see if is is the shortest page yet
    if dict[value] == []:
        l = min(depth,l)
        depth-=1
        return
    #loops through all the elements. 
    for i in dict[value]:
        #adds to a set so there are no repeating values
        seto.add(1)
        seto.add(i)
        #recursive function. Its depth first search, so it'll be in the first iteration of depth one until it reaches the end
        #the depth will go up by 1
        search(i, depth+1)
        #makes sure when the end of a list is reached, it'll return or else the program will automatically termiante
        if dict[value].index(i) + 1 == len(dict[value]):
             #if its the end of a list, and its the list of page 1, then break, or else return will skip the if conditions below
             if value == 1:
                  break
             depth-=1
             return
    #checks if the length of the set is same as the input to make sure all pages have been traversed through
    if len(seto) == x:
            boo = True
    #can cut down a few lines of code by printing from the function instead of returning then printing
    if boo:
        return ['Y', l]
    else:
        return ['N', l]
a = search(1, 1)
print(f"{a[0]}\n{a[1]}")
