N = int(input())

s = []
e = []
for _ in range(N):
    a, b = map(int, input().split())
    s.append(a)
    e.append(b)

s.sort()
e.sort()

res = 0
tmp = 0
s_idx = 0
e_idx = 0


while s_idx < N:
    if s[s_idx] < e[e_idx]:
        tmp += 1
        res = max(tmp, res)
        s_idx += 1
    else:
        tmp -= 1
        e_idx += 1


print(res)
