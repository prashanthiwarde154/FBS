# Program to Find the Roots of Quadratic Equation 

a=int(input('Enter Cofficient of x2 (Quadratic cofficient) : '))
b=int(input('Enter cofficient of x (linear cofficient ) : ')) 
c=int(input('Enter Constant Term :'))

# Discriminant
d = (b*b)-(4*a*c)
root1=(-b+d**0.5)/(2*a)
root2=(-b-d**0.5)/(2*a)

print('Roots of quadratic Equation \n Root 1 :',root1 ,'\n Root 2 :',root2)