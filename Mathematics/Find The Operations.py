N, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cells = N * N
A = [[0]*(cells+1) for _ in range(cells)]
for u in range(N):
    for v in range(N):
        row = u*N + v
        A[row][cells] = grid[u][v]

        for x in range(N):
            for y in range(N):
                if abs(u-x) + abs(v-y) <= D:
                    col = x*N + y
                    A[row][col] = 1
r = 0
pivot_col = [-1]*cells
for c in range(cells):
    pivot = -1
    for i in range(r, cells):
        if A[i][c]:
            pivot = i
            break
    if pivot == -1:
        continue
    A[r], A[pivot] = A[pivot], A[r]
    pivot_col[r] = c
    for i in range(cells):
        if i != r and A[i][c]:
            for j in range(c, cells+1):
                A[i][j] ^= A[r][j]
    r += 1
for i in range(r, cells):
    if A[i][cells]:
        print("Impossible")
        exit()
x = [0]*cells
for i in range(r-1, -1, -1):
    col = pivot_col[i]
    val = A[i][cells]
    for j in range(col+1, cells):
        if A[i][j]:
            val ^= x[j]
    x[col] = val
ops = []
for idx, v in enumerate(x):
    if v:
        ops.append((idx//N, idx % N))
print("Possible")
print(len(ops))
for i, j in ops:
    print(i, j)