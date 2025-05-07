def student_grading(score):
   
    if (score >= 70 and score <= 100):
        print("Your grade is A")
    elif (score >= 60 and score <= 69):
        print("Your grade is B")
    elif (score >= 46 and score <= 59):
        print("Your grade is C")
    elif (score >= 45 and score <= 40):
        print("Your grade is D")
    elif (score >= 0 and score <= 44):
        print("Your grade is F")
    else:
        print("Please input a valid number")

print(student_grading(int(input("Enter a score: "))))
