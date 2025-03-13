def factorial(num):
   if num < 0:
    print("Error. Please enter a positive integer.")
    return None
   elif num == 0:
    return 1
   else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
   
#example
number = int(input("Enter a number: "))
result = factorial(number)

if factorial is not None:
    print("The factorial of", number, "is: ", result)