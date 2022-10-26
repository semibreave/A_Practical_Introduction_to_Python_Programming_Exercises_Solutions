"""
2. A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.
"""
#Enhanced with unintentional spacing proof

string = input('Enter a sentence:')

stripped = string.strip()

space = 0
index = -1

for c in stripped:
 index+=1

 if(c == ' '):
  if(stripped[index + 1] != ' '):
   space += 1

print('Total words:',space + 1)

