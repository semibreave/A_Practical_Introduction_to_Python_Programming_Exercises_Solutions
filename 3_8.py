"""
8. Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]

"""

input_seconds = eval(input('Enter number of seconds:'))

minutes = input_seconds // 60

remainder_seconds = input_seconds % 60


print(minutes,'minutes',remainder_seconds,'seconds')
