# 9. Write a program to check if entered number is a palindrome or not.
def check_palindrome(num):
    rev=0
    temp = num
    while(num>0):
        d = num % 10
        rev = rev * 10 + d
        num //= 10
    if(temp == rev):
        print("Number is Palindrome ")
    else : 
        print("Number is Not Palindrome ")

num = int(input("Enter the No. : "))
check_palindrome(num)