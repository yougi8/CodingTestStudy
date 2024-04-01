## 프로그래머스 연습문제 - 둘만의 암호 (99클럽 미들러 문제) level 1
def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    ## 뛰어 넘을 문자열은 공백으로 만들어주기(공백이 아니라 사실상 삭제)
    for i in skip:
        alpha = alpha.replace(i, '')

    for i in range(len(s)):
        change = alpha[(alpha.find(s[i]) + index) % len(alpha)]
        answer += change

    return answer

print(solution('aukks','wbqd',5))

### 문제 풀이
# 뛰어넘을 문자열을 미리 삭제시켜주는 것이 포인트!
# z가 되면 다시 a부터 시작해야 하니까, 알파벳의 길이로 나눈 나머지를 인덱스로 사용하자