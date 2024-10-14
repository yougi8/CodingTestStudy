## 프로그래머스 - Lv3. 순위 https://school.programmers.co.kr/learn/courses/30/lessons/49191
def solution(n, results):
    answer = 0

    ## step1. 주어진 경기 결과 기록하기
    score = [[0] * n for _ in range(n)]

    # 이긴 경우 : 1, 진 경우 : -1
    for win, lose in results:
        score[win - 1][lose - 1] = 1
        score[lose - 1][win - 1] = -1

    ## step2. 주어진 경기 결과로 추측할 수 있는 나머지 선수들의 순위 판단하기
    for player in range(n):  # 중간점
        for i in range(n):  # 시작점
            for j in range(n):  # 끝점
                # 시작점==끝점 이거나, 이미 순위가 명확하다면 패스
                if i == j or score[i][j] == 1 or score[i][j] == -1:
                    continue
                if score[i][player] == 1 and score[player][j] == 1:
                    score[i][j] = 1
                    score[j][i] = -1

    ## step3. 순위가 명확한 선수 카운트하기
    # 본인과 싸우는 경우를 제외하고 판단하므로, 경기 결과에 0이 하나만 있는 경우가 순위 명확한 경우
    for player in score:
        if player.count(0) == 1:
            answer += 1
    return answer

## 문제 풀이
# set을 활용해서 풀어도 되지만, 나는 무식하게 플로이드 워셜로 풀었다.
# a-b의 관계에서 a>c이고 c>b일 경우에는 a>b가 된다는 것을 참고해서 풀면 된다
# 다만 3중 for문을 돌릴 때 어떤 값이 기준이 되는 건지 너무너무 헷갈렸다!