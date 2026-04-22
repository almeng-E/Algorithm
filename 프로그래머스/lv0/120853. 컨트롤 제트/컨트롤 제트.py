def solution(s):
    li=s.split()
    answer=0
    for i in range(len(li)):
        if li[i] != "Z":
            answer+=int(li[i])
        else:
            answer -= int(li[i-1])
    return answer