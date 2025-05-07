#Revision
def numbers():
    for row in range(1, 10):
        for col in range(1, row + 1):
            print(row, end=" ")
        print(" ")
#Calling the function
numbers()