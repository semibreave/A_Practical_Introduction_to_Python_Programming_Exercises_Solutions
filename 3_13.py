"""
13.Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number.

"""
import math

number = eval(input('Enter a number:'))

print('sin:',round( math.sin(number),4 ) ,' cos:',  round(   math.cos(number),4 ),' tan:',  round(   math.tan(number),4 ),sep='' )


    
