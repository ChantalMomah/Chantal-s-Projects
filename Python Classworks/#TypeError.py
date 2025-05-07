#TypeError
#Assign a string to variable a
a = "str"

#Implementing the try block
try:
    #Trying to divide a string by 2
    print(a/2)
#Handling TypeError exception
except TypeError:
    #Print a message when division of a string by 2 is attempted
    print("can't divide a string")

