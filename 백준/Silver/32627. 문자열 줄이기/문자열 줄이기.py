import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
alpha = [[] for _ in range(26)]
for i in range(N):
    alpha[ord(S[i])-97].append(i)
lazy = []
for i in alpha:
    lazy += i
lazy = set(lazy[:M])
res = ''
for i in range(N):
    if i not in lazy:
        res += S[i]
print(res)