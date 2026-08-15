#8. Print 1 to 100 in snakes and ladder pattern.
c = 1
for i in range(1, 11):
    if i % 2 != 0:
        for j in range(1, 11):
            print(c, end=" ")
            c += 1
    else:
        temp = c + 9
        for j in range(1, 11):
            print(temp, end=" ")
            temp -= 1
            c += 1
    print()
