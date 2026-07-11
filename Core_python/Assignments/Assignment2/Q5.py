# 5. WAP to calculate selling price of book based on cost price and discount
cost_price = float(input('Enter Cost Price of Book :'))
dis = float(input('Enter Discount percentage :'))
dis_value = (cost_price*dis)/100
sell_price = cost_price-dis_value
print(f'The book cost {cost_price} and after {dis}% of discount the selling price cost {sell_price}')
