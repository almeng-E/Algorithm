N = int(input())
S = input()
v = {'a', 'e','i','o','u'}
cnt = 0
for c in S:
    if c in v:
        cnt += 1
print(cnt)