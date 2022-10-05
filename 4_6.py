"""
6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
"""


number = eval(input('Enter number of items:'))

if(number < 10):
  print('Total costs:', number * 12)
elif(number < 100):
  print('Total costs:', number * 10) 
else:
  print('Total costs:', number * 7)
