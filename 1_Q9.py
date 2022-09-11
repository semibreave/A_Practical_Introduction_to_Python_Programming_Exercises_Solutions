"""
9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
"""

price = eval(input("Enter meal price:"))
percent_tip = eval(input("Enter percent tip:"))

print ('Tip Amount:',round(percent_tip/100 * price ,2))
print ('Total Bill:',round((100 + percent_tip)/100 * price,2))
