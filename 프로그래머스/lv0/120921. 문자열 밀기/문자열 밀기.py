def solution(A, B):
    cnt = 0
    while A!=B:
        if cnt> len(A):
            return -1
        A=A[-1]+A[:-1]
        cnt+=1
    return cnt