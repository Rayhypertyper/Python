a = int(input())
for i in range(a):
    b = int(input())
    a = 1
    waitlist = []
    arr = []
    for i in range(b):
        x = int(input())
        arr.append(x)
    while True:
        if len(arr) > 0 and arr[-1] == a:
            a+=1
            arr.pop()
        elif len(waitlist) >=1 and waitlist[-1] == a:
            a+=1
            waitlist.pop()
        else:
            waitlist.append(arr[-1])
            arr.pop()
        if len(arr) == 0 and len(waitlist) == 0:
            print('Y')
            break
        elif len(arr) == 0 and waitlist[-1] != a:
            print('N')
            break