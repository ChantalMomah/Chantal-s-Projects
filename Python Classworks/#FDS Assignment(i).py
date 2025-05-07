#FDS Assignment
def linear_sum(arr, n):
    #If array has only one element, return that element
    if n == 1:
        return arr[0]
    # Recursive case: Sum the current element with the sum of the rest of the array
    else:
        return arr[n - 1] + linear_sum(arr, n - 1)

# Define the array A 
firstName = "Chantal"
Surname = "Momah"
concatenated_name = firstName + Surname
ascii_values = [ord(char) for char in concatenated_name]

# Compute the sum of the array A
result = linear_sum(ascii_values, len(ascii_values))
print("Sum of the ASCII values:", result)