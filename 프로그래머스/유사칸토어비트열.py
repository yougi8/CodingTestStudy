## 프로그래머스 - 유사 칸토어 비트열 Lv.2 https://school.programmers.co.kr/learn/courses/30/lessons/148652
def solution(n, l, r):
    answer = 0

    def cantor(num):
        if (num % 5) == 2:
            return 0
        if (num < 5):
            return 1
        return cantor(num // 5)

    for i in range(l - 1, r):
        if cantor(i):
            answer += 1
    return answer

## 문제 풀이
# 재귀
# 처음에는 11011 11011 00000 11011 11011 이게 반복된다고 생각하고 코드를 짰는데
# 가운데 있는 00000 때문에 0이 5단위로 무한증식한다!
# 11011을 봤을 때 0은 무조건 가운데에 위치하니까, 5로 나누었을 때 나머지가 2일 경우에 무조건 그 값은 0이다 (인덱스가 01234로 부여됨)
# 그래서 확인하고 싶은 인덱스를 0~4 이내로 데리고 온 후에 판단한다!