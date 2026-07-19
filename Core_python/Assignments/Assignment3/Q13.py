#13. Write a program to input electricity unit charges and calculate total electricity bill
#   according to the given condition:
#   For first 50 units Rs. 0.50/unit
#   For next 100 units Rs. 0.75/unit
#   For next 100 units Rs. 1.20/unit
#   For unit above 250 Rs. 1.50/unit
#   An additional surcharge of 20% is added to the bill

unit = float(input("Enter Your Electricity Bill Unit : "))
if(unit<=50):
    bill = unit*0.50
    charges = bill*0.2
    totalbill=bill+charges
    print("Your Total Bill : ",totalbill)
elif(unit<=100):
    bill = unit*0.75
    charges = bill*0.2
    totalbill=bill+charges
    print("Your Total Bill : ",totalbill)
elif(unit<=200):
    bill = unit*1.20
    charges = bill*0.2
    totalbill=bill+charges
    print("Your Total Bill : ",totalbill)
elif(unit<=250 or unit>250):
    bill = unit*1.50
    charges = bill*0.2
    totalbill=bill+charges
    print("Your Total Bill : ",totalbill)
