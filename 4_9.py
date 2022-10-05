"""
9. Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]

"""


number = eval(input('Enter a number:'))

for i in range(number):

 i = i + 1
 if(number % i == 0):print(i,'is a divisor')
