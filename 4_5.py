"""
5. Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""
import random

number = eval(input('Enter a number:'))

#trying for 50 times
for i in range(50):

 if(number == random.randint(0,10)):

  print('Strucked!')

 else:print('Nope')
