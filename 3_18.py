"""
18. Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]

"""

change = eval(input('Enter amount in cents:'))


pen_start = change % 5
nic_max = change // 5
dim_max = change // 10
qua_max = change // 25

count = 0
match = 0

for pen in range(pen_start,change+1,5):

    for nic in range(nic_max+1):

      for dim in range(dim_max+1):

          for qua in range(qua_max+1):

           count = count + 1
           if(pen*1 + nic*5 + dim*10 + qua*25 == change):
            match = match + 1
            print(pen,'penny',nic,'nickel',dim,'dime',qua,'quarter')
           
print()
print('Change Value:',change,'cents')
print('Total test:',count)
print('Total combo:',match)

"""
else:
 print(pen,nic,dim,qua,'-',count)           
        

"""
