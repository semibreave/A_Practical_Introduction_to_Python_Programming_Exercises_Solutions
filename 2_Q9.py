"""
9. The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.
1,1,2,3,5,8,13,21,34,55,89...

"""

times = eval(input("Enter how many FIBONACCI numbers:"))

p1 = 1
p2 = 1


for i in range(times):
    
     i += 1

     if(i==1 or i==2):

          print(1)

     else:
          fib = p1 + p2
          print(fib)
          p2 = p1   
          p1 = fib
         
