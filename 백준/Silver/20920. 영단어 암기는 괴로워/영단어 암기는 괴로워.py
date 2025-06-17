import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = {}
for _ in range(N):
    s = input().rstrip()
    if len(s) < M:
        continue

    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1

vocab = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in vocab:
    print(i[0])