# Random Practice
cost = float(input("Enter the total cost of the items in your shopping cart: "))
if cost < 50:
    tax = 0
    shipping_charge = 5
elif cost >= 50 and cost <= 100:
    tax = 0.1
    shipping_charge = 10
else:
    tax = 0.15
    shipping_charge = 0
print('Your tax is $', tax, ' and your shipping charge is $', shipping_charge)
total = cost + tax + shipping_charge
print("Your total cost including tax and shipping is $", total)