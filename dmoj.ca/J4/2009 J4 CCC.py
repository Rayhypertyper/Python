while True:
    counto = 0 #to keep track how many of the numbers in arr add up to x not going over x
    arr = [7,2,3,4,4,5]
    count = 0
    brr = ["WELCOME", "TO", "CCC" , "GOOD", "LUCK", "TODAY"]
    x = 15 #int(input())
    for i in range(len(arr)):
        count+=arr[0]
        counto+=1
        if count > x:
            counto-=1
            count-=arr[i]
            break
        arr.pop(0)
    counto1 = counto - 1 #number of spaces 
    crr = [0] * counto1
    acount = 0
    while acount <= counto1:
        for i in range(len(crr)):
            crr[i]+=1
            acount+=1
            if acount == x - count:
                break
    print(brr[0],end='')
    brr.pop(0)
    for i in range(len(crr)):
        print("." * crr[i], end='')
        print(brr[0],end='')
        brr.pop(0)
# counto = 0
# count = 0fdfd
# acount = 0

