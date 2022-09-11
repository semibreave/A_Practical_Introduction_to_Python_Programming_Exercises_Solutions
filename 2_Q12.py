"""
12. Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.
*
**
***
****

"""

high = eval(input("Enter how high:"))


for i in range(high):
    
     i += 1
     print('*' * i)

  
