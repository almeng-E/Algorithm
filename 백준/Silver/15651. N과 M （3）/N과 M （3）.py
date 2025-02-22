def make_product(c_subset):
    if len(c_subset) == M:
        print(*c_subset)
        return


    for i in range(N):
        c_subset.append(nums[i])
        make_product(c_subset)
        c_subset.pop()



N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

make_product([])