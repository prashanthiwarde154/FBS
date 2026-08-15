#9. Write a program to create three lists of numbers, their squares and cubes

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = []
l3 = []
square = 0
cube = 0 

print("List of No.'s : ",l1)
for  i in range(len(l1)):
    square = l1[i] ** 2
    l2.append(square)
    cube = l1[i] ** 3
    l3.append(cube)

print("Square of No.'s : ",l2)
print("Cubes of No.'s : ",l3)