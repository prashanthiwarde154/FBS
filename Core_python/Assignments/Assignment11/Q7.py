#7. Python Program to Find the Intersection of Two Lists
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
        
for i in range(len(l1)-1,-1,-1):
    if (l1[i] not in l2):
        l1.pop(i)
print(l1)