import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque


def in_order(v):
    global cnt
    if v == -1:
        return
    in_order(left[v])

    lvl = depth[v]
    if lvl not in res_dict:
        res_dict[lvl] = [N+1, 0]
    res_dict[lvl][0] = min(res_dict[lvl][0], cnt)
    res_dict[lvl][1] = max(res_dict[lvl][1], cnt)

    cnt += 1
    in_order(right[v])



N = int(input())

left = [-1] * (N+1)
right = [-1] * (N+1)
parent = [0] * (N+1)  # 부모 정보 기록


for _ in range(N):
    n, l, r = map(int, input().split())
    left[n] = l
    right[n] = r
    if l != -1:
        parent[l] = n
    if r != -1:
        parent[r] = n

# 루트 찾기: 부모가 없는 노드가 루트임
root = 0
for i in range(1, N+1):
    if parent[i] == 0:
        root = i
        break

# 깊이 구하기
depth = [0] * (N+1)
queue = deque()
queue.append(root)
depth[root] = 1
while queue:
    v = queue.popleft()
    lv = left[v]
    if lv != -1:
        depth[lv] = depth[v] + 1
        queue.append(lv)
    rv = right[v]
    if rv != -1:
        depth[rv] = depth[v] + 1
        queue.append(rv)


res_dict = {1: [N+1, 0]}

# 노드 별 x값 구하기
cnt = 1
in_order(root)

# 가장 넓은 레벨의 너비 찾기
res_depth = 0
res_width = 0
for key in sorted(res_dict.keys()):
    if res_width < res_dict[key][1] - res_dict[key][0] + 1:
        res_width = res_dict[key][1] - res_dict[key][0] + 1
        res_depth = key


print(res_depth, res_width)