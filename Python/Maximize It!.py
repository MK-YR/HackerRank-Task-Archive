from itertools import product

K, M = map(int, input().split())
lists = []
for _ in range(K):
    lst = list(map(int, input().split()))
    values = set((x*x) % M for x in lst[1:])
    lists.append(values)
max_value = 0
for combo in product(*lists):
    value = sum(combo) % M
    if value == M - 1:
        print(M - 1)
        exit()
    max_value = max(max_value, value)
print(max_value)