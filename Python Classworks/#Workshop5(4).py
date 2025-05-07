def row_column():
    for row in range(1, 11):
        for col in range(1, row+1):       
            print (row, end=" ")
        print(" ")
#Calling the function
row_column()