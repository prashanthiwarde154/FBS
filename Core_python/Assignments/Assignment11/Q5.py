#5. Python Program to Sort a List According to the Length of the Elements
#   within the list.
li = ["apple", "hi", "banana", "cat"]
# print(len(li[0]))
for i in range(len(li)-1):
    for j in range(0,len(li)-1):
        if(len(li[j]) > len(li[j+1])):
            # li[i] , li[i+1] = li[i] , li[i+1]
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
print(li)