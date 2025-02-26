import sys
input = sys.stdin.readline

N = int(input())

info = []
for _ in range(N):
    start, end = map(int, input().split())

    info.append((start, end, end-start))

info.sort(key=lambda x: (x[1], x[0], x[2]))

res = 0
c_idx = 0
while c_idx < N:
    end = info[c_idx][1]
    res += 1
    for i in range(c_idx+1, N):
        if end <= info[i][0]:
            c_idx = i
            break
    else:
        break
print(res)