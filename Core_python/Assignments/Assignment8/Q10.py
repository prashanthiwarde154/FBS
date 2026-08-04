# 10. Write a program to check if entered year is a leap year or not.
def leep_year(num):
    if(num%400==0) or (num%4==0 and num%100!=0):
        print("Leep year ")
    else :
        print("Not Leep Year")

num = int(input("Enter the year : "))
leep_year(num)
