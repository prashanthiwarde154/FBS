#6. Python Program to Find the Union of two Lists
l1 = [2,3,4,5,6]
l2 = [5,6,7,7,8]
l1.extend(l2)
for i in range(len(l1)-1,-1,-1):
    for j in range(i+1):
        if(i!=j and l1[i] == l1[j]):
            l1.pop(i)
print(l1)
