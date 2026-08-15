#7. Write a program to create a new list from existing list which contains cube of
#   each number of list.

def create_new_list(li):
    li2 = []
    cube = 0
    for i in range(len(li)+1):
        cube = i**3
        li2.insert(i,cube)
    print(li2)

li = [1,2,3,4,5,6,7]
create_new_list(li)