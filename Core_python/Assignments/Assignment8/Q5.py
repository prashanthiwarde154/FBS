#5. Sum of all prime numbers between 1 to n
n = int(input("Enter a number: "))

sum_prime = 0
for i in range(2, n + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        sum_prime += i
print("Sum of prime numbers =", sum_prime)