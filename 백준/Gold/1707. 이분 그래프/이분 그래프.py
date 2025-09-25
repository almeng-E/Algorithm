import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, bef):
    c = color[cur]
    for nxt in gr[cur]:
        if nxt == bef:
            continue
        if color[nxt] == c:
            return False
        elif color[nxt] == -1:
            color[nxt] = (c+1)%2
            check = dfs(nxt, cur)
            if not check:
                return False
    return True


T = int(input())

for _ in range(T):
    V, E = map(int, input().split())

    gr = [[] for _ in range(V+1)]
    color = [-1] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        gr[a].append(b)
        gr[b].append(a)

    for i in range(1, V+1):
        if color[i] == -1:
            color[i] = 0
            check = dfs(i, -1)
            if not check:
                break
    else:
        print('YES')
        continue
    print('NO')