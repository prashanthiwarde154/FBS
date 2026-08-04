# 11. WAP to check if a given number is Armstrong number or not. For
#       each task create separate functions.

def check_amstrong(num):
    n=num
    length = len(str(n))
    total = 0
    while(num>0):
        d = num % 10
        pow = d ** length
        num//=10
        total =total+ pow
    if(total == n):
        print("Amstrong")
    else :
        print("Not Amstrong")

num = int(input("Enter No. : "))
check_amstrong(num)