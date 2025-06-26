import sys
input = sys.stdin.readline

# 입력
N, C = map(int, input().split())

depth = [-1] * (N+1)
in_o = [0] * (N+1)
out_o = [0] * (N+1)

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# 순회하며 초기화
# 재귀 깊이... stack DFS
stack = []
stack.append((C, 0, 1, 0))  # (노드, bef, depth, 상태)
while stack:
    cur, bef, dep, st = stack.pop()
    if st == 0:
        cnt += 1
        in_o[cur] = cnt
        depth[cur] = dep
        stack.append((cur, bef, dep, 1))
        for nxt in graph[cur]:
            if nxt == bef:
                continue
            stack.append((nxt, cur, dep+1, 0))
    else:
        out_o[cur] = cnt

# seg-tree (업데이트 카운트 세기)
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

seg_tree = [0] * SIZE

# 쿼리
Q = int(input())
for _ in range(Q):
    cmd, node = map(int, input().split())

    # point-update
    if cmd == 1:
        idx = in_o[node] - 1 + LEN
        seg_tree[idx] += 1
        idx >>= 1
        while idx:
            seg_tree[idx] = seg_tree[idx<<1] + seg_tree[(idx<<1) + 1]
            idx >>= 1

    # range-get
    elif cmd == 2:
        res = 0
        left = in_o[node] - 1 + LEN
        right = out_o[node] - 1 + LEN

        while left <= right:
            if left & 1:
                res += seg_tree[left]
                left += 1
            if not right & 1:
                res += seg_tree[right]
                right -= 1
            left >>= 1
            right >>= 1

        print(res * depth[node])
