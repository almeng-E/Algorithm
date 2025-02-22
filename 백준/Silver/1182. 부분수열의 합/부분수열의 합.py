def make(idx, tmp_subset):
    global N, S, res
    # base case
    if idx == N:
        if sum(tmp_subset) == S and tmp_subset:
            res += 1
        return

    make(idx+1, tmp_subset)
    tmp_subset.append(nums[idx])
    make(idx+1, tmp_subset)
    tmp_subset.pop()

N, S = map(int, input().split())

nums = list(map(int, input().split()))

res = 0
make(0, [])
print(res)