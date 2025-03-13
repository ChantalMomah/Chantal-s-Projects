#Workshop10(1)
#Generate random numbers between 1 to 200 divisible by 5
import random

randomNumbers = [num for num in range(1, 201) if num % 5 == 0]
print("The random numbers divisible by 5: ", randomNumbers)
