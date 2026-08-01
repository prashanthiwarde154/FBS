#7. Write a program to solve the following series :
#   a. 1! + 2! + 3! + 4! + .....n!
#   b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#   c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#   d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#   e. x - x2/3 + x3/5 - x4/7 + .... to n terms

#----A-----
n1 = int(input("Enter no. : "))
fact=1
total=0
for i in range (1,n1+1):
    fact=fact*i
    total=total+fact
print(total)

#-----B-----
n2=int(input("Enter no. : "))
pow=0
for i in range(1,n2+1):
    pow=pow+(n2**i)
print(pow)

#------C---------
n3=int(input("Enter no. : "))
s=0
for i in range(n3):
    s=s+(2**i)
print(s)


#--------D----------
A=int(input("Enter no. : "))
add=0
for i in range(1,10+1):
    res=((A**i)/i)
    add+=res
print(add)

#---------E--------
#   e. x - x2/3 + x3/5 - x4/7 + .... to n terms
n5=int(input("Enter no. : "))
x=int(input("Enter X : - "))
den=1
result=0
for i in range(1,n5+1):
    if i %2 ==0:
        result -= ((x**i)/den)
    else:  
        result += ((x**i)/den)
    den+=2
        
print(result)




