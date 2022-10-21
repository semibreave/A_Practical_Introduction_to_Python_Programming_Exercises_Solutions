"""
1. Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
"""

string = input('Enter a string:')

print('Num of char:',len(string),sep='')

for i in range(10):print(string,end=' ')
print()

print('First char:',string[0])

print('First 3 chars:',string[:3])

print('Last 3 chars:',string[-3:])

print('Reverse String:',string[::-1])

if(len(string) >= 7):print('7th char:',string[7])
else:print('Not long enough')

print('1st & last char removed',string[1:(len(string) -1)])

print(string.upper())

print(string.replace('a','e'))
