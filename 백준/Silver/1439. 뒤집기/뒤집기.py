import sys
S = sys.stdin.readline().rstrip()
cnt = [0, 0]    # 1->0 / 0->1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        continue

    if S[i] == '1':
        cnt[1] += 1
    else:
        cnt[0] += 1

print(max(cnt))