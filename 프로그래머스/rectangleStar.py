## 프로그래머스 연습문제 - 직사각형 별찍기 (99클럽 비기너 문제)
# 별 문자를 이용해 가로가 n 세로가 m인 직사각형 형태 출력하기
# n,m <= 1000 자연수
# 입력 예시
# 5 3
# 출력 예시
# *****
# *****
# *****
import sys
n,m = map(int, sys.stdin.readline().split())

for _ in range(m):
    for _ in range(n):
        print("*", end='')
    print()