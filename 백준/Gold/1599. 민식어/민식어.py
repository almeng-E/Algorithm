import sys
input = sys.stdin.readline

k = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
N = int(input())
token = {}
for i in range(len(k)):
    token[k[i]] = i

t_words = []
for _ in range(N):
    S = input().rstrip()
    t = []
    i = 0
    while i < len(S):
        if S[i] == 'n' and i+1 < len(S) and S[i+1] == 'g':
            t.append(token['ng'])
            i += 2
        else:
            t.append(token[S[i]])
            i += 1
    t_words.append(t)
t_words.sort()
for t in t_words:
    res = []
    for tok in t:
        res.append(k[int(tok)])
    print(''.join(res))