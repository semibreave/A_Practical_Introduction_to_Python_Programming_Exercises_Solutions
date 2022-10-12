"""
12. Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.

"""

import random

score = 0

for i in range(5):
 number = random.randint(1,10)

 user_guess = eval(input('Guess a number(1-10):'))

 if(number == user_guess):
  print('computer:',number,'guess:',user_guess,'correct')
  score += 10

 else:
  print('computer:',number,'guess:',user_guess,'wrong')
  score -= 1


print('Your score:',score)


  
