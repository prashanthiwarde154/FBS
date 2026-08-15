#10. Write a program to print list after removing even numbers.
li = [1,2,3,4,5,6,7,8,9,10]
for i in range ( len(li)-1 ,-1 , -1 ):
    if(i % 2 != 0):
        li.remove(li[i])
print(li)