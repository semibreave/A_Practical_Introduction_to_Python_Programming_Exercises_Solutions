"""
13. In the last chapter there was an exercise that asked you to create a multiplication game for
kids. Improve your program from that exercise to keep track of the number of right and
wrong answers. At the end of the program, print a message that varies depending on how
many questions the player got right.

"""

import random

right = 0
wrong = 0

for i in range(10):
 i = i + 1
 number1 = random.randint(0,10)
 number2 = random.randint(0,10)

 answer = eval(input ('Question '  + str(i) + ': ' + str(number1) + 'x' + str(number2) + ' = ' ) )

 if(answer == number1 * number2 ):
     right += 1
     print('RIGHT!')
 else:
     wrong += 1
     print('WRONG.',' The answer is ', number1 * number2)

print()

print('Number of right answers:', right)

print('Number of wrong answers:', wrong)
    
