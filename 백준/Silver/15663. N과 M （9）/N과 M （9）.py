def make(tmp_list):
    if len(tmp_list) == M:
        print(*tmp_list)
        return


    for i in my_nums.keys():
        if my_nums[i] > 0:
            my_nums[i] -= 1
            tmp_list.append(i)
            make(tmp_list)
            tmp_list.pop()
            my_nums[i] += 1


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

my_nums = dict()
for i in arr:
    if i not in my_nums:
        my_nums[i] = 1
    else:
        my_nums[i] += 1


make([])