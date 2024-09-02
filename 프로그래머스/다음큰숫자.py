## 프로그래머스 - Lv2. 다음 큰 숫자 https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    answer = 0

    binary_num = bin(n)  # 이진수로 바꿔주는 함수 bin()
    count = binary_num.count('1')  # 이진수에서 1 개수 카운트

    cnt = n + 1  # 다음 큰 숫자의 후보는 n+1부터 1,000,000까지

    while True:
        if bin(cnt).count('1') == count:  # 숫자 후보의 이진수 1의 개수가 n이 가진 갯수와 같다면 리턴
            return cnt
        else:  # 아니면 그 다음 숫자 살펴보기
            cnt += 1
    return answer

## 문제 풀이
# bin()이라는 이진수 만드는 함수를 모르면 풀기 어려운 문제
# bin() 하면 앞에 0b가 붙고 이진수값이 나온다. 그래서 제대로 이진수값을 찾으려면 [2:] 이렇게 해줘야함
# 이진수 만드는 내장함수 사용하지 않고 이진수로 변환하는 방법
# n을 2로나눈 나머지를 계속 기록. 이때 n을 2로 나눈 몫으로 계속 진행한다.
# def solution(n):
#     answer = 0
#
#     def tobinary(n,arr):
#         rest = n%2
#         q = n//2
#         arr.append(rest)
#         if q==0:
#             return arr
#         else:
#             return tobinary(q,arr)
#     binary_n = tobinary(n,[])
#     count = binary_n.count(1)
#
#     cnt = n+1
#     while True:
#         temp = tobinary(cnt,[])
#         if temp.count(1) == count:
#             return cnt
#         else:
#             cnt += 1
#
#     return answer