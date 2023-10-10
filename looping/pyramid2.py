# for row in range(1, 7):                  
#     for sp in range(7 - row, 1, -1):      
#         print(end=" ")
#     for col in range(row):
#         if (col+row==7  or  col-row==5 or row==6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


for row in range(1, 7):                  
    for sp in range(7 - row, 1, -1):      
        print(end=" ")
    for col in range(row): #1=0,1 2=0,1,2 3=0,1,2,3  4=0,1,2,3,4  5=0,1,2,3,4,5
        if col == 0 or col == row - 1 or row == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()