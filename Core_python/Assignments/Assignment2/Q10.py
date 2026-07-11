#10.WAP to reverse three digit number 

num=int(input('Enter 3 Digit number to reverse the Digit :'))
numm=num
a=num%10  #3
R1=a*100  #300
num=num//10   #14
b=num%10  #4
R2=b*10  #40
num=num//10  #1
R3=num*1  #1
print(f'The {numm} is the 3 digit no. & its Reverse is :{R1+R2+R3}')