# 12. Write a program to check if given number is Armstrong number or not.
n= int(input("Enter No. : "))
num=n
length= len(str(n))
total = 0
while (n>0):
    d=n%10
    pow=d**length
    total=total+pow
    n=n//10
if(num==total):
    print("Armstrong Number")
else:
    print("Not Armstrong No.")