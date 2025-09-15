import sys
input = sys.stdin.readline
def main():
    N = int(input())
    target = [int(input()) for _ in range(N)]
    t_idx = 0

    stack = [0]
    s_val = 1
    res = []
    while stack and s_val <= N and t_idx < N:
        nextNum = target[t_idx]
        stackTop = stack[-1]

        if stackTop < nextNum:
            # 더 쌓아야 됨
            if nextNum < s_val:
                res.clear()
                stack.clear()
                break
            stack.append(s_val)
            res.append('+')
            s_val += 1
        elif stackTop == nextNum:
            res.append('-')
            stack.pop()
            t_idx += 1
        elif stackTop > nextNum:
            res.clear()
            stack.clear()
            break

    if not stack:
        print('NO')
        return

    if s_val <= N:
        print('NO')
        return

    for i in range(len(stack)-1, 0, -1):
        if stack[i] == target[t_idx]:
            res.append('-')
            t_idx += 1
        else:
            print('NO')
            return

    for r in res:
        print(r)


main()