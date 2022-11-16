"""
5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.

"""


string_input = input('Enter list of strings seperate by space:')

L = string_input.split()

M = []

for i in range(len(L)):
    M.append(L[i][1:])

print(M)


