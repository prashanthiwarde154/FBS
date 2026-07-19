#2. WAP to print all odd numbers until n.
n = int(input("Enter the no. : "))
for i in range(n):
    if(i%2!=0):
        print("Even",i)