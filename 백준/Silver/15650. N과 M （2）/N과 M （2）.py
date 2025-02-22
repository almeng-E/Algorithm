def make_combinations(c_index, c_subset):
    if len(c_subset) == M:
        print(*c_subset)
        return

    if c_index < N:
        c_subset.append(nums[c_index])
        make_combinations(c_index+1, c_subset)
        c_subset.pop()
        make_combinations(c_index+1, c_subset)



N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

make_combinations(0, [])