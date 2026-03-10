A = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]
I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
def matmul(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    return result
def scalarmul(c, M):
    return [[c * M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
A2 = matmul(A, A)
for x in range(-10, 10):
    for y in range(-10, 10):
        result = matadd(matadd(A2, scalarmul(x, A)), scalarmul(y, I))
        if result == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
            print(x)
            print(y)
            break