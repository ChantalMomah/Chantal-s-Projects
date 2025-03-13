#Question2(Exception Handling)
def initialize_List():
    List = []
    for i in range(1,10):
        List.append(i)

    return List

#calling the function
result = initialize_List()
print("Initialized List: ", result)