#6. Write a program to remove duplicates from the list.
def rmv_duplicate(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i] == li[j]):
                li.pop(j)
                break
    print(li)
li = [1,2,3,3,5,6,7,7,5]
rmv_duplicate(li)