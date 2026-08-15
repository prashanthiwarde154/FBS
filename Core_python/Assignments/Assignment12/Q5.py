# 5. Python Program to Count the Number of Vowels in a String
str = "hello world how are you"
count=0
for j in range(len(str)):
    if(str[j] == 'a' or str[j] == 'e' or str[j] == 'i' or str[j] == 'o' or str[j] == 'u' ):
        count+=1
print("No. of Vowels in  String : ",count)