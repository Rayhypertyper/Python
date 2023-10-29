# x = 1
# def jamal(x):
#     x+=1
#     return x
# print(jamal(x))

# for i in range(12):
#     for j in range(12):
#         print(i*j)

# flist = [1,2,3]
# slist = ["a","b","c"]
# def listcombine(flist, slist):
#     arr = []
#     for i in range(len(flist)):
#         arr.append(flist[i])
#         arr.append(slist[i])
#     return arr
# print(listcombine(flist, slist))
        
n = int(input())
m = int(input())
p = int(input())
if m <= n :
    print(1+int((n-m)/p))
else:
    print(0)

def socks(list):
    count = 0
    my_dict = dict()
    for i in list:
        if i not in my_dict:
            my_dict[i] = 1
        elif i in my_dict:
            my_dict[i]+=1
    for j in my_dict:
        count+=int(my_dict[j]/2)
    return count
print(socks(list))
