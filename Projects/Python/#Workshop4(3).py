#vowel or consonant
letter = input("Enter a letter of the alphabet: ")
if letter.lower() in ['a','e','i','o','u']:
    print("The letter"+letter+"is a vowel.")
elif letter.isalpha():
    print("The letter"+letter+"is a consonant")
else:
    print("Please enter a letter")
