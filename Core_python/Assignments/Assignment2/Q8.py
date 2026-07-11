# 8.Write a program to swap two number using third variable 
a= int(input('Enter num 1 :-'))
b= int(input('Enter num 2 :-'))
print(f'Numbers Befor Swaping A = {a} , B = {b}')
temp=a
a=b
b=temp
print(f'Numbers After Swaping A = {a} , B = {b}')