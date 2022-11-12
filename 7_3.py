"""
3. Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

"""
import random

L = [8,9,10]

L[1] =17

L = L + [4,5,6]

L.remove(L[0])

L.sort()

L =L * 2

L.insert(3,25)

print(L)
