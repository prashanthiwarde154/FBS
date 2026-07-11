# 11.Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amouont

amount =int(input('Enter amount :'))

n500 = amount // 500
amount = amount %500
n200 = amount // 200
amount = amount %200
n100 = amount // 100
amount = amount %100
n50 = amount // 50
amount = amount %50
n20 = amount // 20
amount = amount %20
n10 = amount // 10
amount = amount %10
n5 = amount // 5
amount = amount %5
n2 = amount // 2
amount = amount %2
n1 = amount

print('500 Notes = ',n500)
print('200 Notes = ',n200)
print('100 Notes = ',n100)
print('50 Notes = ',n50)
print('20 Notes = ',n20)
print('10 Notes = ',n10)
print('5 Notes = ',n5)
print('2 Notes = ',n2)
print('1 Notes = ',n1)
