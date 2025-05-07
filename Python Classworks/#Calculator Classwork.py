class Calculator:
    def main(self):
        while True:
            print("Select an operator: ")
            print("Addition, Division, Average, Modulus, Multiplication or Subtraction")
            operator = input("Input your operator of choice: ")

            num1 = int(input("Enter your first number of choice: "))
            num2 = int(input("Enter your second number of choice: "))

            if operator == 'Addition':
                result = num1 + num2
                print("The result of the addition is: ", result)
            elif operator == 'Division':
                result = num1/num2
                if num1 == 0:
                    print("Error")
                if num2 == 0:
                    print("Error")
                print("The result of the division is: ", result)
            elif operator == 'Average':
                result = (num1 + num2)/2
                print("The result of the average is: ", result)
            elif operator == 'Modulus':
                result = num1%num2
                print("The result of the modulus is: ", result)
            elif operator == 'Multiplication':
                result = num1*num2
                print("The result of the multiplication is: ", result)
            elif operator == 'Subtraction':
                result = num1 - num2
                print("The result of the subtraction is: ", result)

Calculate = Calculator()
Calculate.main()
