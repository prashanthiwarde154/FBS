#4. Python Program to Find the Second Largest Number in a List Using Bubble
#   Sort.

li = [7,6,5,4,9,3,2,1,15]
for i in range(0,len(li)-1):
    for j in range(0,len(li)-i-1):
        if(li[j] > li[j+1]):
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
    print(li)
    print("Second Largest Element of List :-",li[len(li)-2])

