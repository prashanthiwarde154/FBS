# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
A1 = int(input("Enter Angle 1 for Triangle : "))
A2 = int(input("Enter Angle 2 for Triangle : "))
A3 = int(input("Enter Angle 3 for Triangle : "))
if(A1 == A2 and A2 == A3 and A1 == A3 and (A1+A2+A3 == 180)):
    print("The Triangle is Equilateral")
elif((A1 == A2 or A2 == A3 or A1 == A3) and (A1+A2+A3 == 180)) :
    print("The Triangle is Isosceles ")
elif(A1 != A2 and A2 != A3 and A1 != A3 and (A1+A2+A3 == 180)):
    print("The Triangle is Scalene ")
else:
    print("It is Not-Valid Triangle ")