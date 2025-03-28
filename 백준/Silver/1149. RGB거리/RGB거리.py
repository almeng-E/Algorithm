import sys
input = sys.stdin.readline
'''
그리디 접근이 가능한가 ? -> 아님. 각 단계 별 최적의 선택이 전체의 최적해를 보장하지 못함
굳이 탑다운 고민할 필요 없이 바텀업으로 접근
R -> (G or B), 로 생각하면 완전 탐색으로 풀어야 할 것 같음 ==> 백트래킹, 가지치기 인가?? 싶지만 경우가 너무 많은 것 같음...
반대로
이전의 값들 -> R 칠하는 경우 를 생각해보면 DP로 풀이가 가능함을 알 수 있음
즉 (G or B) -> R 칠하기로 생각하기.

R의 경우만 점화식을 작성해본다면 : 
R[N] = max( G[N-1] , B[N-1] ) + aR[N]   (N >= 1)
(N번쨰에 R을 칠하는 경우는~ 으로 생각하는게 포인트)

POINT : R -> (G or B)  VS (G or B) -> R
i 지점에서 i+1 바라보기 VS i 지점에서 i-1 바라보기 
        완탐           VS         DP, memo
'''


N = int(input())

R = []
G = []
B = []
# 초기 테이블 설정
cost = list(map(int, input().split()))
R.append(cost[0])
G.append(cost[1])
B.append(cost[2])
for i in range(1, N):
    cost = list(map(int, input().split()))
    R.append(min(G[i - 1], B[i - 1]) + cost[0])
    G.append(min(R[i - 1], B[i - 1]) + cost[1])
    B.append(min(R[i - 1], G[i - 1]) + cost[2])

print(min(R[N-1], G[N-1], B[N-1]))