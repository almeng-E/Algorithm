from itertools import permutations
N = int(input())
nPm = permutations(range(1, N+1), N)
for perm in nPm:
    print(*perm)