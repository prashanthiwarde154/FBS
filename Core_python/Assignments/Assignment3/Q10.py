#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input("Enter Your Gender (Male/Female) :")
age = int (input("Enter Your age :"))
if(gender == 'Male'):
    if(age>=21):
        print("Your are Eligible for Marriage ")
    else:
        print("Your are Not-Eligible for Marriage ")
elif(gender == 'Female'):
    if(age>=18):
        print("Your are Eligible for Marriage ")
    else:
        print("Your are Not-Eligible for Marriage ")
else:
    print("Invalid gender Entered .!!")