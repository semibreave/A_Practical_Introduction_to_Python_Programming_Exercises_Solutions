"""
Print a box like the one below.
*******************
*                 *
*                 *
*******************
"""



for rows in range(4):
    for columns in range(19):

            if(rows == 0 or rows == 3):
                print("*", end='')
            else:
                if(columns == 0 or columns == 18):
                    print("*",end='')
                else:
                    print(' ',end='')    
                

    print()
