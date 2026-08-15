#2. Write a program to find maximum and minimum element in a list.

def min_max(li):
    min = li[0]
    max = li[0]
    for i in range(0,len(li)):
        if(li[i] < min):
            min = li[i]
        if(li[i] > max):
            max = li[i]
    print("Minimum of the List :-",min)
    print("Maximum of the List :-",max)

li=[6,5,4,3,1,18,9,2]
min_max(li)