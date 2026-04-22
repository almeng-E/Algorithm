def solution(today, terms, privacies):
    answer = []
    # today 일자 저장
    t_year,t_month,t_day=map(int,today.split('.'))
    
    # term 저장
    term_dict= dict()
    for term in terms:
        a,b= term.split()
        term_dict[a]=int(b)
    
    #privacies 저장
    p_list=[]
    for p in privacies:
        p_date,p_term=p.split()
        p_year,p_month,p_day=map(int,p_date.split('.'))
        p_list.append([p_year,p_month,p_day,p_term])
    
    
    #계산
    for ch in p_list:
        ch[2]-=1       #day수정
        if ch[2]==0:
            ch[2]=28
            ch[1]-=1
            if ch[1]==0:
                ch[1]=12
                ch[0]-=1
        ch[1]+=term_dict[ch[3]] #month 수정
        while ch[1]>12:
            ch[0]+=1
            ch[1]-=12
    
    #datecheck
    for i,ch in enumerate(p_list):
        if t_year>ch[0] or (t_year==ch[0] and t_month>ch[1]) or (t_year==ch[0] and t_month==ch[1] and t_day>ch[2]):
            answer.append(i+1)

    
    
    return answer