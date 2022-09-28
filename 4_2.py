"""
2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
ature is in. Your program should convert the temperature to the other unit. The conversions
are F = 9
5 C + 32 and C = 5
9(F − 32).

"""

value = eval(input("Enter value:"))

unit = input("Enter tempreature unit:")

if(unit == 'c'):

 F = 9 / 5 * value + 32 
 print(F)

elif(unit in 'f'):
 C = 5/9 * (value - 32)
 print(round(C,3))

