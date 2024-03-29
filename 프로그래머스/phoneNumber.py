## 프로그래머스 연습문제 - 핸드폰 번호 가리 (99클럽 비기너 문제)
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 * 로 가리기
# phone_number 길이 : 4이상, 20이하
import sys
def solution(phone_number):
    answer = ''
    length = len(phone_number)
    ## 마지막 4자리를 제외하고 앞에서부터 * 로 채워주기
    for i in range(length-4):
        answer += "*"
    ## answer에 마지막 4자리 추가하기
    answer += phone_number[length-4 : length]
    return answer