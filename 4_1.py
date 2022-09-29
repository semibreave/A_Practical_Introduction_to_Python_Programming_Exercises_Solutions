"""
1. Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

"""

cm = eval(input("Enter value in CM:"))


if(cm < 0):
 print('Please enter value greater than 0')

else:
 inch = 2.54 * cm
 print(cm,'cm is equal to',inch,'inch')

