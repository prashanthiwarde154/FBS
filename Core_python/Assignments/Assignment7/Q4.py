for i in range(1,6):    
    for j in range(5-i):
        print(" ",end=' ')
    k=i
    for j in range(1,i+1):
        
        print(k,end=' ')
        k=k+1
    k-=2   
    for j in range(i-1,0,-1):
        print(k,end=' ')
        k=k-1
    print()
