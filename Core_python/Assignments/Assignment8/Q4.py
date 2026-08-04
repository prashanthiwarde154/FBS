#4. Sum of all odd numbers between 1 to n
def sum_of_odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i

    print(f'Sum of odd no till {n} is :- {sum}')

n=int(input("Enter No. : "))

sum_of_odd(n)            
