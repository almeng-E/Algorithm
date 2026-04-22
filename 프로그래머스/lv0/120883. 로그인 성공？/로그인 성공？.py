def solution(id_pw, db):
    answer="fail"
    for i,p in db:
        if id_pw[0]==i and id_pw[1]==p:
            return "login"
        elif id_pw[0]==i and id_pw[1]!=p:
            return "wrong pw"
    return answer