A = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]
def multiply(A, B):
    result = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result
def matrix_power(matrix, power):
    result = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    while power > 0:
        if power % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        power //= 2

    return result
A100 = matrix_power(A, 100)
print(A100[0][0])
print(A100[0][1])
print(A100[1][1])
print(A100[2][1])
print(A100[2][2])