"""
12. Write a program that asks the user for a number and prints out the factorial of that number.
"""


number = eval(input('Enter a number:'))

factorial = 1

for i in range(number):
 i += 1
 factorial *= i

print('The factorial for',number,'is',factorial)
 


