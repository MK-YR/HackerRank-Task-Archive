import sys

data = sys.stdin.read().split()
n, a, b = map(int, data[:3])
d = list(map(int, data[3:3+n]))
total = sum(d)
m = n * (n - 1) // 2
lam = -1.0 if n == 2 else (n - 3) / (n - 1.0)
lam_a = 1.0 if n == 2 and a % 2 == 0 else (-1.0 if n == 2 else pow(lam, a))
avg_factor = (n + 4) / (3.0 * n)
base = total * avg_factor
e = list(map(float, d))
for _ in range(b):
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + e[i]
    new_e = []
    for t in range(n):
        len_win = n - t
        sum_win = sum(prefix[p+len_win] - prefix[p] for p in range(t+1))
        c = (t + 1) * (n - t) - 1
        new_e.append(((m - c) * e[t] + (sum_win - e[t])) / m)
    e = new_e
weighted = sum(((k + 1) * (n - k) - 1) * e[k] for k in range(n)) / m
correction = lam_a * (weighted - base)
expected = base + correction
print(f"{expected:.9f}")