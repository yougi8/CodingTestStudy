## 프로그래머스 pccp 모의고사 1회 2번 - 체육대회
def dfs(ability, picked, depth, sum_value):
    global answer
    n = len(ability)
    sports = len(ability[0])

    if depth == sports:
        answer = max(answer, sum_value)
    else:
        for i in range(n):
            if picked[i] == False:
                picked[i] = True
                dfs(ability, picked, depth + 1, sum_value + ability[i][depth])
                picked[i] = False
    return


def solution(ability):
    global answer
    answer = 0

    n = len(ability)
    sports = len(ability[0])
    picked = [False] * n
    #     for i in range(sports):
    #         picked[i] = True

    dfs(ability, picked, 0, 0)
    return answer