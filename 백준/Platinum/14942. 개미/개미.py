import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
ants = [0] + [int(input()) for _ in range(N)]
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 부모, 깊이 찾기 BFS
p = [(-1, 0)] * (N+1)
depth = [-1] * (N+1)
queue = deque()
queue.append(1)
depth[1] = 0
max_depth = 0
p[1] = (1, 0)
while queue:
    x = queue.popleft()
    for nx, weight in graph[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            max_depth = depth[nx]
            p[nx] = (x, weight)
            queue.append(nx)
# sparce-table ( -칸 위, 그 거리 )
LOG = max_depth.bit_length()

up = [[(-1, 0) for _ in range(LOG)] for _ in range(N+1)]

# 2^0칸 채우기
for i in range(1, N+1):
    up[i][0] = p[i]

# 나머지 칸 채우기
for j in range(1, LOG):
    for i in range(1, N+1):
        m_node = up[i][j-1][0]
        dist = up[i][j-1][1]
        up[i][j] = (up[m_node][j-1][0], up[m_node][j-1][1] + dist)


# 이진 리프팅
for i in range(1, N+1):
    room = i
    ant_p = ants[i]
    ant_d = depth[i]
    for j in range(LOG-1, -1, -1):
        # if not (ant_d & (1 << j)):
        #     continue
        m_node, d = up[room][j]
        if m_node == -1 or d > ant_p:
            continue

        ant_p -= d
        room = m_node
    print(room)


