#15. Python Program to find larger string without using built-in functions.
s1 = 'wellcome'
s2 = 'guyss'
count_s1=0
count_s2=0
for i in s1:
    count_s1 += 1
for i in s2:
    count_s2 += 1
if(count_s1 > count_s2):
    print(f'{s1} : String is Greater than : {s2}')
elif(count_s2 > count_s1):
    print(f'{s2} : String is Greater than : {s1}')
else:
    print("Both are equal Strings")