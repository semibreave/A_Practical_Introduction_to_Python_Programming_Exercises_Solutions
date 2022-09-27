"""
16. Below is described how to find the date of Easter in any year. Despite its intimidating appear-
ance, this is not a hard problem. Note that ⌊x⌋ is the floor function, which for positive numbers
just drops the decimal part of the number. For instance ⌊3.14⌋ = 3. The floor function is part
of the math module.
C = century (1900’s → C = 19)
3.8. EXERCISES
25
Y = year (all four digits)
m = (15 + C − ⌊ C
4 ⌋ − ⌊ 8C+13
25
⌋) mod 30
n = (4 + C − ⌊ C
4 ⌋) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d = (19c + m) mod 30
e = (2a + 4b + 6d + n) mod 7
Easter is either March (22+d +e) or April (d +e−9). There is an exception if d = 29 and e = 6.
In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
e = 6, and m = 2,5,10,13,16,21,24, or 39. In this case, Easter falls one week earlier on April
18. Write a program that asks the user to enter a year and prints out the date of Easter in that
year. (See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)
"""



import math


Y = eval(input("Enter year:"))

C = math.floor(Y/100)



m = ( 15 + C - math.floor(C/4) -  math.floor((8*C + 13)/25 ) ) % 30

n = (4 + C - math.floor(C/4)) % 7

a =  Y % 4

b =  Y % 7

c = Y % 19

d = (19*c + m) % 30

e = ((2*a) + (4*b) + (6*d) + n) % 7

print('Y:',Y,' C:',C,' m:',m,' n:',n,' a:',a,' b:',b,' c:',c,' d:',d,' e:',e,sep='')

if(d==29 and e==6):
 print('Easter day: April 19')

elif( d==28 and e==6 and (m==2 or m==5 or m==10 or m==13 or m==16 or m==21 or m==24 or m==39 )  ):
 print('Easter day: April 18')

else:
 print('Easter day:Either March',(22+d+e),'or April',(d+e-9))
