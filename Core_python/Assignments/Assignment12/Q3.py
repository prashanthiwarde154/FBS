#3. Python Program to Detect if Two Strings are Anagrams
str1 = 'listen'
str2 = 'silent'
if sorted(str1) == sorted(str2):
    print("String is Anagram")
else:
    print("String is Not Anagram")

