#Workshop8(1)
def main():
    #opening the file in read mode
    try:
        with open('example.txt', 'r') as file:
            #Go through the contents of the file
            contents = file.read()
            print("The contents of the file: ", contents)
    except FileNotFoundError:
        print("File not found. Make sure the file exists!")


