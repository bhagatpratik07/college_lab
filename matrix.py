# Function to perform matrix multiplication for two 3x3 matrices
def matrix_multiply(mat1, mat2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

# Input: Two 3x3 matrices
matrix1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Output: Displaying the result of matrix multiplication
result_matrix = matrix_multiply(matrix1, matrix2)
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nResult of Matrix Multiplication:")
for row in result_matrix:
    print(row)


# Function to perform matrix multiplication for two 3x3 matrices
# def matrix_multiply(mat1, mat2):
#     result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 result[i][j] += mat1[i][k] * mat2[k][j]

#     return result

# # Input: Two 3x3 matrices
# matrix1 = []
# matrix2 = []

# print("Enter elements of Matrix 1:")
# for i in range(3):
#     row = [int(x) for x in input().split()]
#     matrix1.append(row)

# print("\nEnter elements of Matrix 2:")
# for i in range(3):
#     row = [int(x) for x in input().split()]
#     matrix2.append(row)

# # Output: Displaying the result of matrix multiplication
# result_matrix = matrix_multiply(matrix1, matrix2)

# print("\nMatrix 1:")
# for row in matrix1:
#     print(row)

# print("\nMatrix 2:")
# for row in matrix2:
#     print(row)

# print("\nResult of Matrix Multiplication:")
# for row in result_matrix:
#     print(row)


# INPUT: Enter elements of Matrix 1:
# 2 3 4
# 5 6 7
# 8 9 10

# Enter elements of Matrix 2:
# 1 0 0
# 0 1 0
# 0 0 1


# OUTPUT: Matrix 1:
# [2, 3, 4]
# [5, 6, 7]
# [8, 9, 10]

# Matrix 2:
# [1, 0, 0]
# [0, 1, 0]
# [0, 0, 1]

# Result of Matrix Multiplication:
# [2, 3, 4]
# [5, 6, 7]
# [8, 9, 10]
