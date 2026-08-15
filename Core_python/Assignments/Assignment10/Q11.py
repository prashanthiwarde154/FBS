#11. Write a program to print all numbers which are divisible by m and n in the
#   list.

li = [1,2,3,4,5,6,7,8,9,10]
m=int(input("Enter The M value :-"))
n=int(input("Enter the N value :-"))
mList=[]
nList=[]
for i in range(len(li)):
    if(li[i]%m==0):
        # print(li[i])
        mList.append(li[i])
    if(li[i]%n==0):
        # print(li[i])
        nList.append(li[i])

print(f'M Divisible List {m} :',mList)
print(f'N Divisible List {n} :',nList)