def solution(N, number):
    answer = 0
    DP = [set() for _ in range(9)]
    for i in range(1, 9):
        DP[i].add(int(str(N)*i))    
    
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in DP[j]:
                for op2 in DP[i-j]:
                    DP[i].add(op1 + op2)
                    DP[i].add(op1 - op2)
                    DP[i].add(op1 * op2)
                    if op2 != 0:
                        DP[i].add(op1 // op2)
        if number in DP[i]:
            return i
    return -1