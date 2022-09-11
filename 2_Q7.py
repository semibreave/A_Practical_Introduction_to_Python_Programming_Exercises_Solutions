"""
7. Write a program that uses exactly four for loops to print the sequence of letters below.
AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
"""
for i in range(1):
 print('A'*10,'B'*7,'CD'*4,sep='',end='')
 for i in range(1):
   print('E',end='')
   for i in range(1):
    print('F'*6,end='')
    for i in range(1):
     print('G')
    
