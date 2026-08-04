for i in range(1,6):

    for j in range(5-i):
        print(' ',end=' ')
    for j in range(1):
        print('*',end=' ')
    for j in range(i-1):
        print(' ',end=' ')

    for j in range(1,i-1):
        print(' ',end=' ')
    if i>1:
        for j in range(1,0,-1):
            print('*',end=' ')
    print()

for i in range(1,5):

    for j in range(i):
        print(' ',end=' ')
    for j in range(1):
        print('*',end=' ')
    for j in range(4-i,0,-1):
        print(' ',end=' ')

    for j in range(3-i):
        print(' ',end=' ')
    if i<4:
        for j in range(1):
            print('*',end=' ')
    print()
