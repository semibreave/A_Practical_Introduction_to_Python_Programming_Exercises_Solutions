"""
2. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
"""
count4 = 0

count9 = 0

for i in range(1,101,1):
  i = i ** 2
  if(i%10 == 4):
   count4 = count4 + 1

  elif(i%10 == 9):
   count9 = count9 + 1 
print('End 4:', count4, 'End 9:',count9)



