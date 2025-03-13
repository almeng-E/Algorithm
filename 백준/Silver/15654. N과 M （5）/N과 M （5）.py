def make_permutation(tmp):
    global N, M
    if len(tmp) == M:
        print(*tmp)

    for i in range(N):
        if not used[i]:
            used[i] = 1
            tmp.append(nums[i])
            make_permutation(tmp)
            tmp.pop()
            used[i] = 0



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
used = [0] * N

make_permutation([])