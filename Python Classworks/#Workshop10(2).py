#Workshop10(2)
import random
import string

def generatePassword():
    password = []

    #Add an uppercase letter
    for _ in range(2):
         password.append(random.choice(string.ascii_uppercase))

    #Add a lowercase letter
         for _ in range(2):
               password.append(random.choice(string.ascii_lowercase))

    #Add two numbers
         for _ in range(2):
              password.append(random.choice(string.digits))

    # Fill the remaining characters with random choices
    remaining_length = 10 - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(string.ascii_letters + string.digits))


    random.shuffle(password)
    password = ''.join(password)
    return password

# Generate and print the password
password = generatePassword()
print("Your 10 character generated password is: ", password)