def integerNum(num):
    if num<=0:
        print("Please enter a positive integer")

    numberList = []
    for i in range(1, num + 1):
        numberList.append(i)

    return numberList

#Example
input = int(input("Enter a positive integer: "))
result =integerNum(input)
print("List: ", result) 