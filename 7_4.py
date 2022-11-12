"""
4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.

"""
L = eval(input('Enter list(1-12):'))

for i in range(len(L)):
 if(L[i] > 10):
  L[i]= 10

print(L)
