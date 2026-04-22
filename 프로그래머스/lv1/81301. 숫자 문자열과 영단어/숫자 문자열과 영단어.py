def solution(s):
    l=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(l)):
        s=s.replace(l[i],str(i))

    return int(s)