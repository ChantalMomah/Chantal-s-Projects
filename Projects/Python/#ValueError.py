#ValueError
# Import the sys module to use the sys.exit() function
import sys  

try:
     #Tell the user to enter a number and convert the number to an integer
    number = int(input("Enter a number between 1 - 10: "))
#If the input cannot be converted to an integer
except ValueError:
    # Print a message indicating that only numbers should be entered 
    print("Enter only numbers")  
    # Exit the program using the sys.exit() function
    sys.exit() 
print("You entered number: ", number)  # Print the entered number 