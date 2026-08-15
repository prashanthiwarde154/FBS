# 8. Write a program to create a duplicate of an existing list. It should not point to
#   same list.
def create_duplicate(li):
    temp = li.copy()
    temp.append(60)
    print("Original :-",li)
     
    print("New : ",temp)

li = [1,2,3,4,4,5,5,9,9,10,10]
create_duplicate(li)