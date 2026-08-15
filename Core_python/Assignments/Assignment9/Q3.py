#3. Write a program to reverse a given number using recursive function.

def reverse(n, rev=0):
    if n == 0:
        return rev
    d =n%10
    rev = rev * 10 + d
    return reverse(n//10,rev)


num = int(input("Enter a number: "))
print("Reverse =", reverse(num))