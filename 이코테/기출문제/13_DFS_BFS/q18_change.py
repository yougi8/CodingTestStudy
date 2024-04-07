## 프로그래머스 60058, 이코테 기춝문제 18. 괄호 변환 - dfs/bfs
def balance(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def is_right(u):
    count = 0
    for i in u:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''

    if p == '':
        return answer

    index = balance(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if is_right(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

### 문제 풀이
# 일단 균형잡힌 문자열을 어떻게 판단하는지가 포인트였다! count +1,-1 해서 인덱스 찾기
# 그리고 문자열 앞뒤로 문자 제거할 때 u = u[1,-1] 이렇게 했더니 안됐다. list화 해주기
# 마지막에 answer 합칠 때도 그냥 answer += u 했더니 안됐다. 리스트를 문자열로 합치는거니까 join 사용하기
