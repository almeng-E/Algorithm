N = int(input())

starts = []
ends = []

for _ in range(N):
    # b < c
    _, b, c = map(int, input().split())
    starts.append(b)
    ends.append(c)

starts.sort()
ends.sort()


s_idx, e_idx = 0, 0
res = 0
tmp = 0

while s_idx < N and e_idx < N:

    if starts[s_idx] < ends[e_idx]:
        tmp += 1
        s_idx += 1
        res = max(res, tmp)

    else:
        tmp -= 1
        e_idx += 1


print(res)