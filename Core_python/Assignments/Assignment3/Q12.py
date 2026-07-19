#12. Write a program to check if given 3 digit number is a palindrome or not.
num=int(input("Enter 3 Digit No. : "))  #123
digit=num 
          #temporary store in digit
d1=num%10            #123 % 10 = 3
R1=d1*100
num=num//10

d2=num%10
R2=d2*10
num=num//10

d3=num
R3=d3*1
reverse=R3+R2+R1
if(reverse==digit):
    print("Palindrome")
else:
    print("Not Palindrome")