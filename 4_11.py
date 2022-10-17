"""
11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm

"""

#now is a variable used to store time with every hours added

now = eval(input('Enter hour(1-12):'))

apm= input('Enter am or pm:')

ahead = eval(input('Enter hours ahead:'))


#Convert time to military format 
if( (now != 12) and (apm == 'pm') ):

    now += 12

elif((now == 12) and (apm == 'am')):

   now = 0


#using a loop to add every hours and reset it to 0 every 24 hrs
for i in range(ahead):

 
 now = now + 1

 if(now >= 24):
  now =0

#(Optional)if time now happen to be 0 ,change it to 12 to looks better
if(now==0):now=12


#Convert back to 24 hrs format as required by this question
if(now >12):
  now -= 12
  print('New Hour:',now,'pm' )

else:
  print('New Hour:',now,'am')

   



    
