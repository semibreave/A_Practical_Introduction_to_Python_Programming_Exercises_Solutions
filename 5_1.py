"""
1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
1.
"""
count = 0

for i in range(1,101,1):
  i = i ** 2
  if(i%10 == 1):
   count = count + 1 
print(count)
