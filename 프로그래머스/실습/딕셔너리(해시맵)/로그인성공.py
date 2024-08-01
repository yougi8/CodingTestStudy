## 프로그래머스 교재실습 - 딕셔너리(해시맵) - 로그인 성공? Lv.0
def solution(id_pw, db):
    diction = {i[0]: i[1] for i in db}

    if id_pw[0] in diction:
        if id_pw[1] == diction[id_pw[0]]:
            return 'login'
        return 'wrong pw'
    else:
        return 'fail'

## dictionary 만들고 -> key-value로 확인하기
# defaultdict으로 하려면 :     diction = defaultdict(int,{i[0]: i[1] for i in db}) (collections defaultdict 선언 후 사용)
# 한줄로 말고, key-value로 하려면
# from collections import defaultdict
# def solution(id_pw, db):
#     diction = defaultdict(list)
#     for key, value in db:
#         diction[key].append(value)
#     if id_pw[0] in diction:
#         if id_pw[1] in diction[id_pw[0]]:
#             return 'login'
#         return 'wrong pw'
#     else:
#         return 'fail'