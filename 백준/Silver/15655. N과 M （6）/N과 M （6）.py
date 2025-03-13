
def make_combination(tmp, c_idx):
    global N, M
    if len(tmp) == M:
        print(*tmp)
        return

    if c_idx >= N:
        return


    tmp.append(nums[c_idx])
    make_combination(tmp, c_idx+1)
    tmp.pop()
    make_combination(tmp, c_idx+1)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

make_combination([], 0)
