from collections import deque

T = int(input())
for _ in range(T):
    P = input().rstrip()
    N = int(input())
    arr = deque(list(input().strip('[]').split(',')))

    if N == 0:
        arr = []
    reverse_flag = 0
    error_flag = 0
    for fx in P:
        if fx == 'R':
            reverse_flag ^= 1
        else:
            if not arr:
                error_flag = 1
                break
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()

    if error_flag:
        print('error')
    else:
        if reverse_flag:
            arr.reverse()
        print(f'[{",".join(arr)}]')