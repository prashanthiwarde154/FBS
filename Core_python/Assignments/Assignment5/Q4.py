#4. WAP to print Armstrong number within a given range
num=int(input("Enter Range For Armstrong no's till : "))
for i in range(1,num+1):
    num=i
    length= len(str(i))
    total = 0
    while (i>0):
        d=i%10
        pow=d**length
        total=total+pow
        i=i//10
    if(num==total):
        print(num)

