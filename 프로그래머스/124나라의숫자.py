## 프로그래머스 - Lv2. 124 나라의 숫자
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        change = n % 3
        if change == 0:
            answer += '1'
        elif change == 1:
            answer += '2'
        else:
            answer += '4'
        n //= 3

    new = ''
    for i in range(len(answer) - 1, -1, -1):
        new += answer[i]
    return new

## 풀이
# 3으로 나눌 때 나머지를 가지고 판단하고 싶다면, 판단하는 숫자의 인덱스가 0부터 시작해야 한다!
# 그래서 while문 돌 때마다 n-=1을 해준다
# 그리고 나는 answer에 +=로 추가를 해서 마지막에 뒤집어줘야 하는데,
# 어차피 문자열 덧셈이니까 answer = '2' + answer 이런식으로 더해주면 마지막에 뒤집어주지 않아도 된다.
## 개선코드
# def solution(n):
#     answer = ''
#     while n>0:
#         n -= 1
#         change = n%3
#         if change==0:
#             answer = '1'+ answer
#         elif change==1:
#             answer = '2' + answer
#         else:
#             answer = '4' + answer
#         n //= 3
#
#     return answer