N = int(input())

m = {136: 1_000, 142: 5_000, 148: 10_000, 154: 50_000}
res = 0
for _ in range(N):
    w, _ = map(int, input().split())
    res += m[w]
print(res)
