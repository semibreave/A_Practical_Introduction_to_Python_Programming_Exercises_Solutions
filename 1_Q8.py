"""
8. Write a program that asks the user to enter three numbers (use three separate input state-
ments). Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
"""
a = eval(input("Enter first number:"))

b = eval(input("Enter 2nd number:"))

c = eval(input("Enter 3rd number:"))

total = a + b + c

average = total /3

print('Total:',total)

print('Average:',round(average,2))
