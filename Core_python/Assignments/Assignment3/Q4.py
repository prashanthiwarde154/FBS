#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
A1 = int(input("Enter Angle 1 for Triangle : "))
A2 = int(input("Enter Angle 2 for Triangle : "))
A3 = int(input("Enter Angle 3 for Triangle : "))
if(A1+A2>A3 and A1+A3>A2 and A2+A3>A1 and A1>0 and A2>0 and A3>0 and (A1+A2+A3==180)):
    print("Triangle is valid")
else:
    print("Triangle is Not-Valid")