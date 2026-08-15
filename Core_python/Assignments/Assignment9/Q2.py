#2. Write a program to check if given number is Armstrong or not using recursive
#   function.

def armstrong(n, pw):
    if (n==0):
        return 0
    d =n%10
    return d**pw + armstrong(n // 10, pw)

num=int(input("Enter a number: "))
d=len(str(num))
res=armstrong(num, d)

if (res==num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")