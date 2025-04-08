import sys
input = sys.stdin.readline


# 가치 기준 풀이 : dict 와 update 이용
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

DP = {}
DP[0] = 0

for weight, value in items:
    # 새로운 상태를 담을 dict
    tmp = {}
    for d_v, d_w in DP.items():

        # index-out 체크
        if d_w + weight > K:
            continue

        # 갱신 가능한지 체크
        if (d_v + value) in DP:
            if DP[d_v + value] <= d_w + weight:
                continue
        tmp[d_v + value] = d_w + weight


    DP.update(tmp)

print(max(DP.keys()))