#FDS Assignment(3)
def ReverseArray(A, i, j):
    if i < j:
        # Swap A[i] and A[j]
        A[i], A[j] = A[j], A[i]
        # Recursively call ReverseArray with updated indices
        ReverseArray(A, i + 1, j - 1)
    return A

# Test the implementation with the surname "MOMAH"
surname = list("MOMAH")
print("Original array:", surname)
reversed_surname = ReverseArray(surname, 0, len(surname) - 1)
print("Reversed array:", reversed_surname)