a = 1
b = 1
c = 1
count = 0
for i in range(10):
  a+=1
  b = 0
  for j in range(10):
    b+=1
    c = 0
    for k in range(10):
      c+=1
      if a+b+c <= 10:
        count+=1
print(count)