#7. Write a program to check if user has entered correct userid and password.
userid = 'Prashant123'
password = 'Prashant@143'
id = input("Enter Your User-ID :")
passwd = input("Enter Your Passowrd :")
if(userid == id and password == passwd):
    print("Correct User id and password enterd ..")
else :
    print("InCorrect User id and Password enterd ..")
