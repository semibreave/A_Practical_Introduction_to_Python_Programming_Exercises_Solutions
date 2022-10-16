"""
14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle.

"""
import math


degrees = eval(input('Enter an angle in degrees:'))

print('Sine',degrees,' degrees is',math.sin(math.radians(degrees)))

