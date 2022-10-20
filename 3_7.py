"""
7. Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an
expression with the modulo operator, convert the angle to its equivalent between 0◦ and
360◦
"""
condition =True

while(condition):
 angle = eval(input('Enter angle between -180 to 180 degrees:'))
 if( angle >= -180 and angle <= 180 ):
  condition = False

 else:
  print('Angle between -180 to 180 degrees only')


eq_angle = 0


if(angle >= 0):
    eq_angle = angle

else:
 
 eq_angle = angle + 360

print('Equivalent angle:',eq_angle)

