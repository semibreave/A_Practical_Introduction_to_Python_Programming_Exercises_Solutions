"""
15. Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.

     *
    * *
   *****
  *     *
 *       *


"""

high = eval(input("Enter how high:"))

tri_width = -1

for i in range(high,0,-1):
    
 tri_width += 2

 if((i== high) or (i == (high//2 + 1))):
  print (i * ' ',tri_width * '*',sep='')

 else:
  print (i * ' ','*',(tri_width-2) * ' ','*',sep='')
    
