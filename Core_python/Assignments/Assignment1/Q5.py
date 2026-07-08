# Write a program to enter P , T ,R and calculate Compound Intrest
P = int(input('Enter Principle Amount :'))
T = int(input('Enter Time Period in Years :'))
R = float(input('Enter Rate of Intrest :'))
A = P*(1+R/100)**T
CI = A - P
print("Compound Intrest is :",CI)