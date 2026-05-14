import sys
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
def comb2(x):
    return x * (x - 1) // 2
def comb3(x):
    return x * (x - 1) * (x - 2) // 6
if __name__ == '__main__':
    n = int(input())
    dsu = DSU(n)
    for _ in range(n - 1):
        u, v, color = input().split()
        u = int(u)
        v = int(v)
        if color == 'b':
            dsu.union(u, v)
    component_sizes = {}
    for i in range(1, n + 1):
        root = dsu.find(i)
        component_sizes[root] = component_sizes.get(root, 0) + 1
    total = comb3(n)
    invalid = 0
    for s in component_sizes.values():
        invalid += comb3(s)
        invalid += comb2(s) * (n - s)
    answer = (total - invalid) % MOD
    print(answer)