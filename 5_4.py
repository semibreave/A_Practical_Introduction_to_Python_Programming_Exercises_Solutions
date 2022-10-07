"""
4. Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
"""
total = 0


for i in range(1,2001,1):
    
 if(i%2 == 1):
  total = total + i

 else:
  total = total - i

print ( total )
    
  
