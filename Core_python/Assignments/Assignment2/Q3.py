#3. Convert distance given in feet and inches into meter and centimeter 
feet = float(input('Enter Feet :'))
inches = float(input('Enter Inches : '))
Total_inches = (feet*12)+inches
Met = Total_inches*0.0254
Cent = Total_inches*2.54
print(f'{feet} Feet and {inches} is :- {Met:.2f} Meter and {Cent:.2f} Centimeter')