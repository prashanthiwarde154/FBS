# 6. WAP to calculate total salary of employee based on basic , da = 10% of basic , ta = 12%of basic hra =15% of basic 

base_salary=float(input('Enter your base salary : '))
DA = (base_salary*10)/100
TA = (base_salary*12)/100
HRA = (base_salary*15)/100
total_sal=base_salary+DA+TA+HRA
print(f'Employee base salary was {base_salary} \n After 10% DA :{DA} + 12% TA {TA} + 15% HRA {HRA} \n Total Salary : {total_sal}')
