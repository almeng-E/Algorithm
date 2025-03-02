import sys
input = sys.stdin.readline

N = int(input())

pos_nums = []
neg_nums = []


for _ in range(N):
    num = int(input())
    if num > 0:
        pos_nums.append(num)
    else:
        neg_nums.append(num)

pos_nums.sort(reverse=True)
neg_nums.sort()

res = 0
tmp = 0
for i in range(0, len(pos_nums)):
    # 1 은 규칙 제외
    if pos_nums[i] == 1:
        res += tmp
        tmp = 0
        res += 1
        continue

    if tmp == 0:
        tmp = pos_nums[i]
    else:
        res += (tmp * pos_nums[i])
        tmp = 0
# 남아있는 수 합산
res += tmp
tmp = 0
for i in range(0, len(neg_nums)):
    if tmp == 0:
        tmp = neg_nums[i]
    else:
        res += (tmp * neg_nums[i])
        tmp = 0
res += tmp

print(res)
