#8. Write a program to check whether a number is prime or not using recursion.
def id_prime(num,i=2):
    if (num<2):
        return False
    if(i*i > 2):
        return True
    if(num%i==0):
        return False
    return id_prime(num,i+1)

print(id_prime(1))
    