#5. WAP to print Fibonacci series upto n.
a=-1
b=1
n=int(input("Enter No for fibonacchi series :"))
for i in range (n):
    c=a+b
    print(c)
    a=b
    b=c