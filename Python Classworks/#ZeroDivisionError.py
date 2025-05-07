#ZeroDivisionError
#Try block to divide 0 by 10
try:
    #Attempting the division which will give a ZeroDivisionError
    print(10/0)

#Except block to handle the ZeroDivisionError exception
except ZeroDivisionError:
    #Printing a message that indicates that 0 can't be divided
    print("You can't divivde the number by zero") 