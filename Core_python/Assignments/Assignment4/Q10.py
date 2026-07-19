n = int(input("Enter no. : "))
sum = 0 
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if(n==sum):
    print("Perfect no. ")
else :
    print("Not perfect no. ")
