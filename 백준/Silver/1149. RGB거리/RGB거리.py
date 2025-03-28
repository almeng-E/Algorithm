import sys
input = sys.stdin.readline

N = int(input())

R = []
G = []
B = []
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