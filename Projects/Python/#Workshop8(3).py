#Workshop8(3)
def writeToFile(file_path):
    try:
        with open(file_path, 'w')as file:
            for i in range(1, 11):
                file.write(f"This is line {i}\n")
            print("The file 'output.txt' was written successfully")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    file_path = 'output.txt'
    writeToFile(file_path)
   
if __name__ == "__main__":
    main()