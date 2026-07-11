# 9.WAP to swap two number without using third variable 

a= int(input('Enter num 1 :-'))
b= int(input('Enter num 2 :-'))
print(f'Numbers Befor Swaping A = {a} , B = {b}')
a=a+b
b=a-b
a=a-b
print(f'Numbers After Swaping A = {a} , B = {b}')
