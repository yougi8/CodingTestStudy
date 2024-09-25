## 프로그래머스 Lv2. 택배상자
def solution(order):
    answer = 0
    n = len(order)
    sub = []

    idx = 1
    flag = 0

    while idx <= n:
        sub.append(idx)

        while sub and sub[-1] == order[flag]:
            answer += 1
            sub.pop()
            flag += 1
        idx += 1

    return answer

## 문제 풀이
# 실제 컨테이너에서는 비교하지 않고, 우선 임시 컨테이너로 보낸 후에 임시 컨테이너랑 order랑 비교한다
# idx는 임시 컨테이너로 보낼 상자의 번호이고
# flag는 order에서 몇 번째 상자를 처리할 차례인지를 나타내는 변수이다
# while문은 종료 조건을 항상 잘 생각하기!