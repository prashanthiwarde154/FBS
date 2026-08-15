#5. Accept a number from user and check if this element is present in the list or
#   not. Also tell how many times it is present in the list.

def find_num(li):
    n = int(input("Enter No. :-"))
    count=0
    for i in range(0,len(li)):
        if(li[i] == n):
            count+=1    
    if(count>0):
        print("Number Found ", count ,"Times")
    else:
        print("Number not Found.") 

li = [1,2,3,4,5,6,7,7]
find_num(li)

