#11. WAP to check if given number Strong Number.
n=int (input("Enter no. : "))
num=n
total=0
while(n>0):#143
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    total = total+fact
    n=n//10
if(total == num):
    print("Strong No.  ")
else: 
    print("Not Strong No.")