def printsInReverse(number):
    if len(str(number)) != 5:
        print("The inputted number must be a 5 digit number")
        return
    
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
        
    print("Inputted digits in reversed order: ")
    for digits in reversed(digits):
        print(digits)

#example
number = 59836
printsInReverse(number)