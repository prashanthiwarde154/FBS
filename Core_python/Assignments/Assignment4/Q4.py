#4. WAP to print factorial of a number .
fact=1
n = int(input("Enter the no. : "))
for i in range(1,n+1):
    fact=fact*i
print(fact)