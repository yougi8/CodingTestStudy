## 프로그래머스 실버2 삼각달팽이
def solution(n):
    arr = [[0] * n for _ in range(n)]
    x, y = -1, 0
    value = 1

    for i in range(n):
        for j in range(i, n):
            ## 아래, 오른쪽, 위 셋 중 하나의 방향으로 숫자 할당해주기
            if i % 3 == 0:
                x += 1  # 아래로
            elif i % 3 == 1:
                y += 1  # 오른쪽으로
            else:
                x -= 1  # 위로
                y -= 1
            arr[x][y] = value
            value += 1

    answer = []
    for i in range(n):
        for j in range(0, i + 1):
            answer.append(arr[i][j])
    return answer


## 문제 풀이
# 아래-오른쪽-위 이 패턴을 반복한다는 것을 이용해서 그 순서대로 값을 할당해주면 된다!