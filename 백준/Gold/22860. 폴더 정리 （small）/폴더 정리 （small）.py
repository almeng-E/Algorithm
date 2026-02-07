import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
tree = dict()

for _ in range(N+M):
    P, F, C = input().split()
    if P not in tree:
        tree[P] = []
    if F not in tree:
        tree[F] = []
    tree[P].append((F, int(C)))


def dfs(cur, lst):
    if cur not in tree:
        return 
    for nxt, is_folder in tree[cur]:
        if is_folder:
            dfs(nxt, lst)
        else:
            lst.append(nxt)


Q = int(input())
for _ in range(Q):
    path = input().rstrip().split('/')
    ret = []
    dfs(path[-1], ret)
    print(len(set(ret)), len(ret))