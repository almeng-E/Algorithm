import sys
input = sys.stdin.readline

graph = [[] for _ in range(10001)]


while True:
    try:
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    except:
        break


def dfs(cur, bef, dist):
    global m_node, m_dist
    for nxt, w in graph[cur]:
        if nxt == bef:
            continue
        dfs(nxt, cur, dist + w)

    if m_dist < dist:
        m_node = cur
        m_dist = dist


m_node = 0
m_dist = 0
dfs(1, 0, 0)

cur = m_node
m_dist = 0
dfs(cur, 0, 0)

print(m_dist)