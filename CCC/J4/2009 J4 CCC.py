import sys
arr = [7,2,3,4,4,5]
brr = ["WELCOME", "TO", "CCC" , "GOOD", "LUCK", "TODAY"]
x = int(input())

while True:
    if len(arr) == 0:
        sys.exit()
    maxnumthatcanfitperline = 0
    count = 0
    yt = 1
    for i in range(len(arr)):
        if sum(arr[0:i+1]) + i > x:
            maxnumthatcanfitperline = i
            break
        else:
            maxnumthatcanfitperline = i + 1
    n = x - sum(arr[0:maxnumthatcanfitperline]) #input length minus legnth of letters in that row
    crr = [0]*(maxnumthatcanfitperline-1)
    if len(crr) == 0 and n != 0:
        crr = [0]
    m = True
    while True:
        for i in range(len(crr)):
            crr[i]+=1
            count+=1
            if count == n:
                m = False
                break
        if m == False:
            break
        if len(crr) == 0:
            break
    for i in range(len(crr)+1):
        if i == len(crr):
            try:
                print(brr[i])
                for _ in range(len(crr)+1):
                    arr.pop(0)
                    brr.pop(0)
                if len(arr) == 0:
                    sys.exit()
                break
            except:
                sys.exit()
        print(brr[i],end='')
        dot = '.'
        if maxnumthatcanfitperline == 1:
            arr.pop(0)
            brr.pop(0)
            print(dot*(crr[i]))
            break
        print(dot*(crr[i]), end='')
        


    






































    # x = 15 #int(input())
    # for i in range(len(arr)):
    #     count+=arr[0]
    #     counto+=1
    #     if count > x:
    #         counto-=1
    #         count-=arr[i]
    #         break
    #     arr.pop(0)
    # counto1 = counto - 1 #number of spaces 
    # crr = [0] * counto1
    # acount = 0
    # while acount <= counto1:
    #     for i in range(len(crr)):
    #         crr[i]+=1
    #         acount+=1
    #         if acount == x - count:
    #             break
    # print(brr[0],end='')
    # brr.pop(0)
    # for i in range(len(crr)):
    #     print("." * crr[i], end='')
    #     print(brr[0],end='')
    #     brr.pop(0)
# counto = 0
# count = 0fdfd
# acount = 0

