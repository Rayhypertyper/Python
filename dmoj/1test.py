import time
st = time.time()
for i in range(1000):
    print(i)
    print('hello world')
en = time.time()
print(en-st)