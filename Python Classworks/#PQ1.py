#PQ1
import random
def guessNumber():
    targetNumber = random.randint(1, 9)

    while True:
        guess = int(input("Guess a number between 1 and 9: "))

        if guess == targetNumber:
            print("You are right!")
        else:
            print("Try again!")

if __name__ == "__main__":
  guessNumber()