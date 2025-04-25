def solution(numbers, target):
    answer = 0
    
    N = len(numbers)
    
    for bit in range((1<<N) -1):
        tmp = 0
        for i in range(N):
            if bit & 1 << i:
                tmp += numbers[i]
            else:
                tmp -= numbers[i]
        if tmp == target:
            answer += 1  
    
    
    
    
    return answer