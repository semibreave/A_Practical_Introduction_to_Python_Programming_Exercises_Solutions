"""
4. Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
"""

credit = eval(input('Enter number of credits:'))

if(credit <= 23):
    print('freshman')
elif(credit <= 53):
    print('sophomore')
elif(credit <= 83):
    print('junior')
else:
    print('senior')
    
