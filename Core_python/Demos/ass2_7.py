num=int(input('Enter 3 Digit number for sum of three Digit :'))
a=num%10
num=num//10
b=num%10
num=num//10
print(a+b+num)