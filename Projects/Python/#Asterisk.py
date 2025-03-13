#file
filename = 'exer1.py'
txt = open(filename)
print("Here's your file: ", filename)
print (txt.read)
print ("Type the filename again: ")
file_again = input("> ")
txt_again = open(file_again)
print (txt_again.read)
    

