import sys
input = sys.stdin.readline

N = int(input())
data = dict()
for _ in range(N):
    S = input().rstrip()
    for i in range(1, len(S)+1):
        if i not in data:
            data[i] = dict()

        if S[:i] not in data[i]:
            data[i][S[:i]] = []

        data[i][S[:i]].append(S)
for length in sorted(data.keys(), reverse=True):
    detail = data[length]
    for k, v in detail.items():
        if len(v) >= 2:
            print(v[0])
            print(v[1])
            break
    else:
        continue
    break