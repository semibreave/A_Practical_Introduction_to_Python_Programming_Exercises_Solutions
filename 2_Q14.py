"""
14. Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.
     *
    ***
   *****
  *******
   *****
    ***
     *

"""

high = eval(input("Enter how high:"))

star = -1

for i in range(high,0,-1):
    
     star += 2

     print (i * ' ',star * '*')
    

for j in range(high-1):

     j+=2

     star -= 2

     print(j * ' ' ,star * '*')
          
