#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
n = int(input("Enter No. : "))
for i  in range(n+1):
    if(i%7==0 and i%5==0):
        print(i)