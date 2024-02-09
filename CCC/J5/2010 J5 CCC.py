leastcount = 10000000
def hop(depth,startx,starty,endx,endy):
    global leastcount
    if startx == endx and starty == endy:
        if depth < leastcount:
            leastcount = depth

    if depth == 6 or startx < 1 or startx > 8 or starty < 1 or starty > 8:
        depth-=1
        return
    
    hop(depth+1,startx+1,starty+2,endx,endy)
    hop(depth+1,startx+1,starty-2,endx,endy)
    hop(depth+1,startx-1,starty+2,endx,endy)
    hop(depth+1,startx-1,starty-2,endx,endy)
    hop(depth+1,startx+2,starty+1,endx,endy)
    hop(depth+1,startx+2,starty-1,endx,endy)
    hop(depth+1,startx-2,starty+1,endx,endy)
    hop(depth+1,startx-2,starty-1,endx,endy)
    return leastcount
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(hop(0,x[0],x[1],y[0],y[1]))