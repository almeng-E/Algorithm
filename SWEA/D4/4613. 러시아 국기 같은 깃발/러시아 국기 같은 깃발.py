def count_color(color, color_list):
    tmp = 0
    for line in color_list:
        tmp += line.count(color)

    return tmp




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # print(flag)

    max_v = 0
    for i in range(1, N - 2 + 1):
        for j in range(i + 1, N - 1 + 1):
            cnt = 0
            white = flag[:i]
            blue = flag[i:j]
            red = flag[j:]
            # print(white, blue, red)

            cnt += count_color('W', white)
            # print(cnt)
            cnt += count_color('B', blue)
            # print(cnt)
            cnt += count_color('R', red)
            # print(cnt)
            max_v = max(max_v, cnt)
    print(f'#{tc} {N*M - max_v}')