from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))


LIS = []
prev_path = [-1] * N
lis_idx = []

LIS.append(arr[0])
lis_idx.append(0)

for i in range(1, N):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
        # 복원용
        prev_path[i] = lis_idx[-1]
        lis_idx.append(i)


    else:
        t_idx = bisect_left(LIS, arr[i])
        LIS[t_idx] = arr[i]
        # 복원용
        lis_idx[t_idx] = i
        if t_idx > 0:
            prev_path[i] = lis_idx[t_idx-1]

last = lis_idx[-1]
actual_LIS = []
while last != -1:
    actual_LIS.append(arr[last])
    last = prev_path[last]
actual_LIS.reverse()
print(len(actual_LIS))
print(*actual_LIS)