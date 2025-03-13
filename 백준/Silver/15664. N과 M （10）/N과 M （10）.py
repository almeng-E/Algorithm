def make(tmp_list, start_idx):
    if len(tmp_list) == M:
        my_nums.add(tuple(tmp_list))
        return


    for i in range(start_idx, N):
        tmp_list.append(arr[i])
        make(tmp_list, i+1)
        tmp_list.pop()



N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

my_nums = set()

make([], 0)

my_nums = list(my_nums)
my_nums.sort()
for i in my_nums:
    print(*i)