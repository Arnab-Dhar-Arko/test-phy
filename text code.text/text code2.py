def matrix_transp(A):
    # Get the number of rows and columns in the original matrix
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    
    # Create a new matrix for the transposed result
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = A[i][j]
    
    return transposed

# Example usage:
A1 = [[1, 2], [3, 4]]
A2 = [[1, 2], [3, 4], [5, 6]]

print(matrix_transp(A1))  # Output: [[1, 3], [2, 4]]
print(matrix_transp(A2))  # Output: [[1, 3, 5], [2, 4, 6]]