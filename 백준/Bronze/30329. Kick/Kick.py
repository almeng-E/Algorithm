S = input().rstrip()
cnt = 0
for i in range(len(S)):
    if S[i:i+4] == 'kick':
        cnt += 1
print(cnt)