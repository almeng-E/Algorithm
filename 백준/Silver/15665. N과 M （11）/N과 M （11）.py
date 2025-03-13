def make(tmp_list):
    if len(tmp_list) == M:
        print(*tmp_list)
        return

    for i in range(len(arr)):
        tmp_list.append(arr[i])
        make(tmp_list)
        tmp_list.pop()


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))




make([], )