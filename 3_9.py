"""
9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.
An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock

"""

hour = eval(input('Enter hour:'))

ahead = eval(input('How many hours ahead?'))

new_hour = (hour + ahead) % 12


print('New hour:',new_hour,"o'clock")
