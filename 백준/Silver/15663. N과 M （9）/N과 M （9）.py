def make(tmp_list):
    if len(tmp_list) == M:
        my_combs.add(tuple(tmp_list))
        return


    for i in range(N):
        if not used[i]:
            used[i] = True
            tmp_list.append(arr[i])
            make(tmp_list)
            tmp_list.pop()
            used[i] = False


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

used = [0] * N

my_combs = set()

make([])

my_combs = list(my_combs)
my_combs.sort()
for i in my_combs:
    print(*i)