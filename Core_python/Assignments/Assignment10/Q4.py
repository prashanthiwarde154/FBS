#4. Write a program to reverse the list.

#Technique 1
def reverseList(li):
    for i in range(len(li)-1,-1,-1):
        print(li[i])

li=[1,2,3,4,5,6,7]
# reverseList(li)

#Technique 2
li.reverse()
print(li)