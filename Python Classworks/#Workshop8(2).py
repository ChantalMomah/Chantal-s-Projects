#Workshop8(2)
import os

def deleteFile(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' was not found")
    except PermissionError:
        print(f"You have permission to delete '{file_path}'.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    file_path = input("Enter the file path to be deleted: ")
    deleteFile(file_path)
if __name__ == "__main__":
    main()