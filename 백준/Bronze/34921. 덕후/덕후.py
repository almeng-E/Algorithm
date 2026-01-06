a, b = map(int, input().split())
p = 10 + 2 * (25 - a + b)
print(p if p >= 0 else 0)