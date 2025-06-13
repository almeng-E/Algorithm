import sys
input = sys.stdin.readline 




def backtrack(idx, mask, g_cnt):
    global max_songs, res

    if idx == N:
        covered = bin(mask).count('1')
        if max_songs == covered:
            res = min(g_cnt, res)
        elif max_songs < covered:
            max_songs = covered
            res = g_cnt
        return

    backtrack(idx+1, mask | gtrs[idx], g_cnt+1)
    backtrack(idx+1, mask, g_cnt)


N, M = map(int, input().split())
max_songs = 0
res = float('inf')
gtrs = []
for _ in range(N):
    _, s = input().split()
    mask = 0
    for i in range(M):
        if s[i] == 'Y':
            mask |= (1 << i)
    gtrs.append(mask)

backtrack(0, 0, 0)

if max_songs == 0:
    print(-1)
else:
    print(res)