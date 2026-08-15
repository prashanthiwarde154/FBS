#11. Python Program to replace every blank space with hyphen in a string.
str="703 A Wing Vrindavan Yewalewadi Pune Maharashtra"
for i in range(len(str)):
    if (str[i] == " "):
        res = str.replace(str[i] ,"-")
print(res)