def make(tmp_list, start_idx):
    if len(tmp_list) == M:
        print(*tmp_list)
        return

    for i in range(start_idx, len(arr)):
        tmp_list.append(arr[i])
        make(tmp_list, i)
        tmp_list.pop()


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))


make([], 0)