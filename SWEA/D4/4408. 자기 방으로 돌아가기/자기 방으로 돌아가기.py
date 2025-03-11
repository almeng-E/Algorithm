T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    start = []
    end = []
 
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        start.append((a - 1) // 2)
        end.append((b - 1) // 2)
 
    start.sort()
    end.sort()
 
    cnt = 0
    res = 0
    s_idx = 0
    e_idx = 0
 
    while s_idx < N and e_idx < N:
        if start[s_idx] <= end[e_idx]:
            cnt += 1
            s_idx += 1
            res = max(res, cnt)
        else:
            cnt -= 1
            e_idx += 1
 
    print(f'#{tc} {res}')