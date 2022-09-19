"""
19. Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
rectangle and a 4 × 8.
0 1 2 3 4
5 6 7 8 9
0 1 2 3 4
0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
"""

number = -1

width = eval(input('Enter width:'))

height = eval(input('Enter height:'))


for i in range(height):


  for j in range(width):

     number += 1
     print(number%10,' ',end='')

  print()

 
 


