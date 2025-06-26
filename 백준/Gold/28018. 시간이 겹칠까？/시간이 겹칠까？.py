import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

imos = [0] * 1_000_002

for _ in range(N):
    S, E = map(int, input().split())

    imos[S] += 1
    imos[E+1] -= 1

for i in range(1, 1_000_001):
    imos[i+1] += imos[i]

_ = int(input())
queries = list(map(int, input().split()))
write('\n'.join(str(imos[q]) for q in queries))
