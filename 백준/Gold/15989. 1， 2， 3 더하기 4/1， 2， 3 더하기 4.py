import sys
input = sys.stdin.readline

T = int(input())
ans = [0] * T
q = []
for i in range(T):
    q.append((int(input()), i))
q.sort()

ones = [0, 1, 1, 2]
zeros = [0, 0, 1, 1]

for i in range(4, q[-1][0]+1):
    ones.append(ones[i-1] + zeros[i-1])
    zeros.append(zeros[i-2])
    if i % 3 == 0:
        zeros[i] += 1

for n, idx in q:
    ans[idx] = str(ones[n] + zeros[n])

print('\n'.join(ans))