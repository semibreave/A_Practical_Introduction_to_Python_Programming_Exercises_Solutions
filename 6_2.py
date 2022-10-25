"""
2. A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.
"""

string = input('Enter a sentence:')

space = 0

for c in string:
 if(c == ' '):
  space += 1
  

print('Total words:',space + 1)
