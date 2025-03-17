N = int(input())
liquid = list(map(int, input().split()))

st = 0
ed = N-1

min_val = max(abs(liquid[0]), abs(liquid[-1])) * 2 + 1
result = []

while st < ed:
    S = liquid[st]
    E = liquid[ed]
    tmp = abs(S + E)

    if tmp == 0:
        result = [liquid[st], liquid[ed]]
        break
    if min_val > tmp:
        min_val = tmp
        result = [liquid[st], liquid[ed]]

    if abs(S) >= abs(E):
        st += 1
    else:
        ed -= 1

print(*result)