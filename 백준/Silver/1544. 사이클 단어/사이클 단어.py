words = set()
N = int(input())
res = 0
for _ in range(N):
    s = input().rstrip()
    if s in words:
        continue
    ns = s+s
    res += 1
    l = len(s)
    for i in range(l):
        words.add(ns[i:i+l])
print(res)