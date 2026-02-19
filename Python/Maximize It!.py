from itertools import product

K, M = map(int, input().split())
lists = []
for _ in range(K):
    lst = list(map(int, input().split()))
    lists.append(lst[1:])
max_value = 0
for combo in product(*lists):
    value = sum(x*x for x in combo) % M
    if value > max_value:
        max_value = value
print(max_value)