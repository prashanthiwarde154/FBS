# Write a program to calculate the percentage of students based on marks of any 5 subjects 
print("Enter Marks for your 5 Subjects :-")
sub1 = int(input("Math :"))
sub2 = int(input("Science :"))
sub3 = int(input("Chemistry :"))
sub4 = int(input("Physics :"))
sub5 = int(input("Biology :"))
total = sub1+sub2+sub3+sub4+sub5
per=(total/500)*100
print('You have got ',per ,'Percentage')
