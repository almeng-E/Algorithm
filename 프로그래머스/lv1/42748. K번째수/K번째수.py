def solution(array, commands):
    answer = []

    for a in range(len(commands)):
        i,j,k=commands[a][0],commands[a][1],commands[a][2]
        li= array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    
    
    return answer