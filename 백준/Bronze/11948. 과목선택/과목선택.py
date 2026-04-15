import sys;input=sys.stdin.readline;
s = [int(input()) for _ in range(6)]
print(sum(s) - min(s[:4]) - min(s[4:]))