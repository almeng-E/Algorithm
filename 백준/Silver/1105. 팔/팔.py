import sys
L, R = sys.stdin.readline().split()
if len(L) == len(R):
    cnt = 0
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)
else:
    print(0)