#7. Find the sum of three digit number

num=int(input('Enter 3 Digit number for sum of three Digit :'))
numm=num
a=num%10
num=num//10
b=num%10
num=num//10
print(f'The {numm} is the 3 digit no. & its sum is :{a+b+num}')