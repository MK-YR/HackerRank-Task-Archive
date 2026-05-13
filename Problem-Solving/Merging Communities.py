def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
n, q = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)
for _ in range(q):
    command = input().split()
    if command[0] == 'M':
        a = int(command[1])
        b = int(command[2])
        union(a, b)
    else:
        a = int(command[1])
        print(size[find(a)])