"""
7. An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.
"""

number = eval(input("Enter a number:"))  

sf = True

for i in range(2,number + 1,1):
 if(number % i == 0):
  
  root = i ** 0.5
  
  if(int(root) ** 2 == i):
   sf = False
   
   break


if(sf):
 print(number,'is a square free')

else:
 print(number,'is not a square free')



