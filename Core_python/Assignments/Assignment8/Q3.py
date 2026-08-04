#3. Write a program to find sum of following series using functions :

#   a. 1+ 2 + 3 + 4+..... + n
def sum_of_range(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    print(f'Sum of Range is :- {sum}')

sum_of_range(5)

#b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f'Factorial is :- {fact}')

factorial(5)

#c. 1^1 + 2^2 + 3^3+ ...... n^n
def exponential_sum(n):
    exp=1
    for i in range(1,n+1):
        exp+=(n**i)
    print('Output:-',exp)

exponential_sum(5)