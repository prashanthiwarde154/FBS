#7. Write a program to find sum of digits using recursion.
def sum_of_digit(num):
    if(num==0):
        return 0
    else:
        d = num%10
        return d+sum_of_digit(num//10)

print(sum_of_digit(133))