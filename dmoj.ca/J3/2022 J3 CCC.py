x = list(input())
a = [b for b in x]
for i in x:
    if i == '+':
        print(' tighten ', end='')
        continue
    elif i == '-':
        print(' loosen ', end='')
        continue
    try:
        if i.isnumeric() == True:
            print(i, end='')
            continue
    except:
        print('\n')

    print(i, end='')
    