#6.Write a program to calculate profit or loss.
Cost_price = int(input("Enter The Cost price :"))
Sell_price = int(input("Enter The Selling price :"))
if(Sell_price>Cost_price):
    print("Profit")
elif(Sell_price==Cost_price):
    print("No Profit ,No Loss")
else:
    print("Loss")