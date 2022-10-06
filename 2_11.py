"""
11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
*******************
*                 *
*                 *
*******************
"""
height = eval( input('Enter height:') )
width = 19

for i in range(height):
  if(i==0 or i== height-1):
   
    print('*' * width)

  else:
   
    print('*' * 1, ' ' * (width-2) , '*' * 1,sep='')
