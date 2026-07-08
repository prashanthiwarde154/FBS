# Write a program to convert days into years , weeks and days
days=int(input("Enter Days :"))
year=days//365
weeks=(days%365)//7
days=(days%7)%7
print(f'Years : {year} , Weeks : {weeks} , Days : {days}')
