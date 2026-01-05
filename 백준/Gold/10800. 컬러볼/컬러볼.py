import sys
input = sys.stdin.readline


N = int(input())
balls = []
for i in range(N):
    c, s = map(int, input().split())
    balls.append((c, s, i))

balls.sort(key=lambda x: x[1])

out = [0] * N
c_sum = [0] * (N+1)
total = 0
for r in range(N):
    c, s, i = balls[r]
    total += s
    c_sum[c] += s
    out[i] = total - c_sum[c]
    l = r-1
    while l>=0 :
        if balls[l][1] == s:
            if balls[l][0] != c:
                out[i] -= balls[l][1]
            l -= 1
        else:
            break
print('\n'.join(map(str, out)))