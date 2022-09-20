"""
17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.
"""

end = eval(input('Enter the final year:'))

ly= 0



for year in range(1600,(end + 1)):

    if(year%4 == 0):
        if(year%100 == 0):
            if(year%400 == 0):
                print(year,'is leap year')
                ly = ly + 1
            else:
                print(year,'not a leap year')
                
        else:
            print(year,'is a leap year')
            ly = ly + 1
    else:
        print(year,'not a leap year')


print('Total:',ly)

