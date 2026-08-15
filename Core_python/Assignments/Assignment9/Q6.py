#   6. Write a program to print Fibonacci series using recursion.
def fib(n):
    if n<=0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))