import sys
input = sys.stdin.readline
N = int(input())
used = set()
cnt = 0
for _ in range(N):
    s = input().rstrip()
    if s == "ENTER":
        used.clear()
        continue
    if s in used:
        continue
    used.add(s)
    cnt += 1
print(cnt)