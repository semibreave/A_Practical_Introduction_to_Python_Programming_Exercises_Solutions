  """
10.
(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power.
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power.
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.

"""

print('a.)')

power = eval(input('Enter power:'))

result = 2 ** power

last = result % 10

print('Result:',result,',','Last Digit:',last)

print()

#######################################################################
print('b.)')

power = eval(input('Enter power:'))

result = 2 ** power

last = result % 100

print('Result:',result,',','Last Two Digits:',last)

print()

######################################################################
print('c.)')

power = eval(input('Enter power:'))

num_digit = eval(input('Enter number of digit:'))

result = 2 ** power

last = result % (10 ** num_digit)

if( len(str(last)) != num_digit ):

    leading_zero = num_digit - len(str(last)) 

    print('Result:',result,',' , 'Last ' , num_digit,' Digits:' , leading_zero * '0',last,sep='')

   
else:
    print('Result:',result,',','Last', num_digit ,'Digits:',last)


                                  
