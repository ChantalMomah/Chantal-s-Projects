def linear_sum(a, n):
    if n == 0:
        return A[0]
    else:
        return A[n] + linear_sum(A, n - 1)

name = 'YourFirstNameYourSurname'
A = [ord(char) for char in name]
n = len(A) - 1

total_sum = linear_sum(A, n)
print("Sum of the sequence of array A: ", total_sum)