"""
3. Write a program that generates a random number between 1 and 10 and prints your name
that many times.

"""

from random import randint

x = randint(1,10)

times = 0

for i in range(x):
 times += 1   
 print('CCP ',times,'x',sep='' )
