#1. Write a program to prompt user to enter userid and password. If Id and
#   password is incorrect give him chance to re-enter the credentials. Let him try 3
#   times. After that program to terminate.
userid='rahul'
password=1821
ch=2
for i in range(1,4):
    id=input("Enter User Id :")
    passwd=int(input("Enter Password : "))
    if(id==userid and password==passwd):
        print("Your Entered Id and Password is Correct !!")
        break
    else:
        print("Entered Id and Password is Incorrect ! \n")
        print(f'{ch} Left...')
        ch-=1