import sys
input = sys.stdin.readline
N = int(input())

est = [int(input()) for _ in range(N)]
est.sort(reverse=True)
tip = 0
for i in range(N):
    if est[i] - i > 0:
        tip += est[i] - i
    else:
        break
print(tip)
