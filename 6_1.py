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
(k) The string with every letter replaced by a space
"""

string = input('Enter a string:')
#a
print('Num of char:',len(string),sep='')

#b
for i in range(10):print(string,end=' ')
print()

#c
print('First char:',string[0])

#d
print('First 3 chars:',string[:3])

#e
print('Last 3 chars:',string[-3:])

#f
print('Reverse String:',string[::-1])

#g
if(len(string) >= 7):print('7th char:',string[6])
else:print('Not long enough')

#h
print('1st & last char removed',string[1:(len(string) -1)])

#i
print(string.upper())

#j
print(string.replace('a','e'))

#k
for c in string:
    print(' ',end='')

