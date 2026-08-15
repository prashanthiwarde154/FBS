#13. Python Program to count number of digits and letters in a string.
str = "Prashant143"
countaplh = 0
countnum = 0
for i in range(len(str)):
    if(str[i].isalpha() == True):
        countaplh += 1
    elif(str[i].isdigit () == True):
        countnum += 1
print(str)
print("Alphabets :- ",countaplh)
print("Numbers :- ",countnum)