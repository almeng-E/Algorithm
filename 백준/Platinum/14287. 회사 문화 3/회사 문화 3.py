import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

p = [0] + list(map(int, input().split()))
for i in range(2, n + 1):
    graph[p[i]].append(i)
offset = [0] * (n+1)

# 오일러 경로 테크닉
cnt = 0
in_o = [0] * (n + 1)
out_o = [0] * (n + 1)

# DFS
stack = []
stack.append((1, 1))  # cur, status(1-진입 0-탈출)
while stack:
    cur, go_in = stack.pop()
    if go_in:
        cnt += 1
        in_o[cur] = cnt
        stack.append((cur, 0))
        for nxt in graph[cur]:
            stack.append((nxt, 1))
    else:
        out_o[cur] = cnt

LEN = 1
while LEN < n:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE

out = []
for _ in range(m):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        i, w = cmd[1:]
        idx = in_o[i] + LEN - 1
        while idx:
            tree[idx] += w
            idx >>= 1

    elif cmd[0] == 2:
        i = cmd[1]
        res = 0
        l, r = in_o[i] + LEN- 1, out_o[i] + LEN - 1
        while l <= r:
            if l % 2 == 1:
                res += tree[l]
                l += 1
            if r % 2 == 0:
                res += tree[r]
                r -= 1
            l //= 2
            r //= 2
        out.append(str(res))

print('\n'.join(out))