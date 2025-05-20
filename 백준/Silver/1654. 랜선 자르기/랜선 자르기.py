import sys
input = sys.stdin.readline

from collections import Counter

K, N = map(int, input().split())

arr = list(int(input()) for _ in range(K))
counted = Counter(arr)

l = 1
r = max(counted)
res = 0
while l <= r:
    middle = (l+r)//2
    tmp = 0
    for length, cnt in counted.items():
        tmp += (length // middle) * cnt
    if tmp >= N:
        res = middle
        l = middle + 1
    else:
        r = middle - 1
print(res)




# 완전 탐색 방식 (최적화 전)
# K, N = map(int, input().split())
# 
# arr = list(int(input()) for _ in range(K))
# res = 0
# for i in range(max(arr), -1, -1):
#     tmp = 0
#     for j in arr:
#         tmp += (j//i)
#     if tmp >= N:
#         res = i
#         break
# print(i)

# 이분 탐색 (최적화 후)


