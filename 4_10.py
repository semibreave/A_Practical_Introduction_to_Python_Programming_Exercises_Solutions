"""
10. Write a multiplication game program for kids. The program should give the player ten ran-
domly generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong.
The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.

"""

import random

for i in range(10):
 i = i + 1
 number1 = random.randint(0,10)
 number2 = random.randint(0,10)

 answer = eval(input ('Question '  + str(i) + ': ' + str(number1) + 'x' + str(number2) + ' = ' ) )

 if(answer == number1 * number2 ):
     print('RIGHT!')
 else:
     print('WRONG.',' The answer is ', number1 * number2)
