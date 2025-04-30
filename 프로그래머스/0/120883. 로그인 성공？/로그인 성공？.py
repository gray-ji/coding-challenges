def solution(id_pw, db):
    for d in db:
        if d[0] == id_pw[0]:
            return 'login' if d[1] == id_pw[1] else 'wrong pw'
                
    return 'fail'