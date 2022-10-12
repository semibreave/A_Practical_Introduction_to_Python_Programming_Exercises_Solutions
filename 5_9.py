"""
9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.

"""

non_s = 0
non_c = 0
non_f = 0

for i in range(1000):

 i += 1

 s_root = i ** 0.5
 c_root = i ** (1/3)
 f_root = i ** (1/5)

 if(int(s_root) ** 2 != i):
  non_s += 1
  

 if(int(c_root) ** 3 != i):
  non_c += 1
  

 if(int(f_root) ** 5 != i):
  non_f += 1
  

print('Non perfect squares count:',non_s)
print('Non perfect cubes count:',non_c)
print('Non perfect 5th powers count:',non_f)

