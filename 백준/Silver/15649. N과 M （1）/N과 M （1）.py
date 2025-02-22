from itertools import permutations

N, M = map(int, input().split())
nPr = list(permutations([i for i in range(1, N+1)], M))
for perm in nPr:
    print(*perm)