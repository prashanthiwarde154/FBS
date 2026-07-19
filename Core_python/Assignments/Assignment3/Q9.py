#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
A = int(input("Enter Marks For Sub 1 : "))
B = int(input("Enter Marks For Sub 2 : "))
C = int(input("Enter Marks For Sub 3 : "))
D = int(input("Enter Marks For Sub 4 : "))
E = int(input("Enter Marks For Sub 5 : "))
per = ((A+B+C+D+E)/500)*100
if(per<=100 and per>=80):
    print("First Class")
elif(per<= 79 and per>= 60):
    print("Second Class")
elif(per<=59 and per>=40):
    print("Third Class")
else:
    print("Fail")