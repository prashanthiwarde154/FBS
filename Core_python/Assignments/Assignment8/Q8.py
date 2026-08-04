# 8. Write a program find reverse of a number
def num_reverse(num):
    rev=0
    while(num>0):
        d = num%10
        rev = rev * 10 + d
        num//=10
    print(rev)

num=int(input("Enter no. : "))
num_reverse(num)
            