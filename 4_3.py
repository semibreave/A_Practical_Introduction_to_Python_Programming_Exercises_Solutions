"""
3. Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is
below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point.
"""

temp = eval(input('Enter tempreature in Celcius:'))

if(temp < -273.15):print('Tempreature is invalid')

elif(temp == -273.15):print('Tempreature is absolute 0')

elif(temp < 0):print('Tempreature is below freezing')

elif(temp == 0):print('Tempreature is at freezing point')

elif(temp < 100):print('Tempreature is at normal range')

elif(temp == 100):print('Tempreature is at boiling point')

else:print('Tempreature above boiling point')                    
