#12. Python Program to count number of lowercase characters in a string.
str = "PrashantHiwarde"
count = 0
for i in range(len(str)):
    if(str[i].islower() == True):
        count +=1
print(count)