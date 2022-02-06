inputo = int(input())
outputo = int(input())
x = inputo
divisor = 1
factorcounter = 0
numcounter = 0



while True:
    if x % divisor == 0:
        factorcounter+=1
    if x == divisor and factorcounter == 4:
        numcounter+=1
        x+=1
        divisor = 0
        factorcounter = 0
        c = factorcounter
    elif x == divisor:
        x+=1
        divisor = 0
        factorcounter = 0
        c = factorcounter
    divisor+=1
    if x == outputo + 1:
        break

print("The number of RSA numbers between " + str(inputo) + " and " + str(outputo) + " is " + str(numcounter))
  
