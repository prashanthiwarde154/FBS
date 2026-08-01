#2. Enter number of students from user. For those many students accept marks of 5
#   subject marks from user and calculate percentage. Display all percentage and
#   average percentage of students.

Stud_count=int(input("Enter The No. of Students : "))
stud=1
for i in range(1,Stud_count+1):
    print(f'Enter 5 subjects Marks of Student {stud} : ')
    sub1=int(input("Math : "))
    sub2=int(input("Science : "))
    sub3=int(input("Biology : "))
    sub4=int(input("Chemistry : "))
    sub5=int(input("Physics : "))
    per=((sub1+sub2+sub3+sub4+sub5)/500)*100
    print("Your Percentage : ",per)
    print('----------------------------------------------------------')
    stud+=1