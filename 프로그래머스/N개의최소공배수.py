## 프로그래머스 - N개의 최소공배수 https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    for i in range(len(arr) - 1):
        a = arr[i]
        b = arr[i + 1]

        arr[i + 1] = lcm(a, b)

    return arr[-1]

## a와b의 최소공배수 = (a*b)//(a,b 최대공약수)
## 최대공약수 gcd 구하는 법 외우기
# while b>0:
#   a,b = b,a%b
# return a

## math.gcd 사용하는 코드
# import math
# def solution(arr):
#     def lcm(a,b):
#         return (a*b)//math.gcd(a,b)
#
#     for i in range(len(arr)-1):
#         a = arr[i]
#         b = arr[i+1]
#         arr[i+1] = lcm(a,b)
#     return arr[-1]