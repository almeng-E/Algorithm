import sys
input = sys.stdin.readline

N, M = map(int, input().split())

DNAs = [input() for _ in range(N)]
DNAs.sort()
my_DNA = ''
idx = {'A': 0, 'C':1, 'G':2, 'T':3}
for j in range(M):
    cnt = [0] * 4
    for i in range(N):
        cnt[idx[DNAs[i][j]]] += 1
    m_idx = cnt.index(max(cnt))
    if m_idx == 0:
        my_DNA += 'A'
    elif m_idx == 1:
        my_DNA += 'C'
    elif m_idx == 2:
        my_DNA += 'G'
    else:
        my_DNA += 'T'
res = 0
for i in range(N):
    for j in range(M):
        if my_DNA[j] != DNAs[i][j]:
            res += 1
print(my_DNA)
print(res)