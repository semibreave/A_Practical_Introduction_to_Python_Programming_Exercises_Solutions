"""
7. Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
"""

x = eval(input('Enter 1st number:'))

y = eval(input('Enter 2nd number:'))

if( round(abs(x - y ),3 ) ==  0.001):print('close')

else:print('not close')

    
