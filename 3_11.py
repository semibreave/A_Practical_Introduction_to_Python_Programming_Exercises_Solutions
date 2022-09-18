"""
11. Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
"""


kg = eval(input('Enter a value in KG:'))

pound = round(kg * 2.20462,1)

print(kg,' KG is ',pound,' pound',sep='')

                                
