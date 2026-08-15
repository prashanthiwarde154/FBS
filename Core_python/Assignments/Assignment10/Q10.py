#10. Write a program to remove all occurrences of a given element in the list.

li=[1,2,7,4,3,2,7,9,3]
el = int(input("Enter the element :"))
for i in range(len(li)-1,-1,-1):
    if(li[i] == el):
        li.remove(li[i])
print(li)