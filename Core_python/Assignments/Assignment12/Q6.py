# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen
str = input("Enter String : ")
for i in range(len(str)):
    if (str[i] == " "):
        res = str.replace(str[i] ,"-")
print(res)