#9. Write a program of having n number of elements in the list and find out even
#   and odd elements in that list and then create two separate lists which will have
#   even elements and other will have odd elements.
li=[]
even=[]
odd=[]
n=int(input("Enter the Range of List :-"))
for i in range(0,n):
    El = int(input("Enter List Elements :-"))
    li.append(El)
print(li)
for i in range(0,len(li)):
    if(li[i]%2==0):
        even.append(li[i])
    else:
        odd.append(li[i])
print("Even List :-",even)
print("Odd List :-",odd)