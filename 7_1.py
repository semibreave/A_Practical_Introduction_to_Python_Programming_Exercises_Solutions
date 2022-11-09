"""
1. Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.
(g) Print how many integers in the list are less than 5.
"""

L = eval(input('Enter list of integers:'))

print('Total items of list:',len(L))

print('Last items of list:',L[len(L) - 1])

L.reverse()
print('Reversed list:',L)
   



    
