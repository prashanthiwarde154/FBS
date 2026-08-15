#1. Write a program to find sum of all elements of list
def sum_of_list(li):
    sum=0
    for i in range(0,len(li)):
        sum = sum + li[i]
    print("Sum of the List :-",sum)

li = [1,2,3,4,5]
sum_of_list(li)