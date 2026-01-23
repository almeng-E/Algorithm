import sys
input = sys.stdin.readline
def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    M = int(input())
    Q = []

    for i in range(M):
        l, r = map(int, input().split())
        Q.append((l, r, i))


    compressed = dict()
    coords = set(arr)
    for i, v in enumerate(coords):
        compressed[v] = i
    # 딕셔너리 look-up을 최대한 줄여보자. 
    # 여기서 미리 변환해서 가져가기.
    for i in range(1, N+1):
        arr[i] = compressed[arr[i]]

    sqrtN = int(N ** 0.5)
    # snake sort를 해보자
    Q.sort(key=lambda x: (x[0] // sqrtN, x[1] if x[0]%sqrtN == 0 else -x[1]))
    ans = [0] * M
    used = [0] * len(coords)
    cnt = 0
    l, r = 1, 0

    for ql, qr, i in Q:
        while r < qr:
            r += 1
            v = arr[r]
            if used[v] == 0:
                cnt += 1
            used[v] += 1

        while r > qr:
            v = arr[r]
            if used[v] == 1:
                cnt -= 1
            used[v] -= 1
            r -= 1

        while ql < l:
            l -= 1
            v = arr[l]
            if used[v] == 0:
                cnt += 1
            used[v] += 1

        while ql > l:
            v = arr[l]
            if used[v] == 1:
                cnt -= 1
            used[v] -= 1
            l += 1

        ans[i] = cnt

    print('\n'.join(map(str, ans)))
main()