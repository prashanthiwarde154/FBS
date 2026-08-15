#14. Python Program to count the occurrences of ach word in a string.

s = "hello world hello python world hello"

words = s.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)