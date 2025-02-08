import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 누적 2차원 배열 생성
li = [[0 for _ in range(m+1)]]
for i in range(n):
    li.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        li[i][j] += li[i-1][j] + li[i][j-1] - li[i-1][j-1]


# 실행부분
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(li[x][y] - li[x][j-1] - li[i-1][y] + li[i-1][j-1])



