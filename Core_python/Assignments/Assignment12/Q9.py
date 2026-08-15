# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
str = "hello prashant hiwarde"
countword = 1
countchar = 0
# print(str.isalpha())
for i in range(len(str)):
    if(str[i] == " "):
        countword += 1
    else:
        countchar += 1
print("Words : ",countword)
print("Characters : ",countchar)
