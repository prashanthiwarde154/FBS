#8. Write a program to prompt user to enter userid and password. After verifying
#   userid and password display a 4 digit random number and ask user to enter the
#   same. If user enters the same number then show him success message otherwise
#   failed. (Something like captcha)
import random
userid = 'Prashant123'
password = 'Prashant@143'

id = input("Enter Your User-ID :")
passwd = input("Enter Your Passowrd :")
if(userid == id and password == passwd):
    captcha = random.randint(1000,9999)
    print("Captcha Code :" ,captcha)
    code = int(input("Enter Given Captcha Code to Login Successfully : "))
    if(captcha == code):
        print("Login Successfull ")
    else:
        print("In-correct captcha ")
    
else :
    print("InCorrect User id and Password enterd ..")