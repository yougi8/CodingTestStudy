## 프로그래머스 - 기능개발 Lv2 (99 미들러 문제)

import math


def solution(progresses, speeds):
    answer = [0] * 100
    release = []  # 며칠 뒤에 배포 가능한지

    for i in range(len(progresses)):
        remain = 100 - progresses[i]  # 완료까지 남은 퍼센트
        release.append(math.ceil(remain / speeds[i]))

    cnt = 0
    max = release[0]
    answer[0] += 1
    for i in range(1, len(release)):
        if release[i] <= max:
            answer[cnt] += 1
        else:
            cnt += 1
            answer[cnt] += 1
            max = release[i]
    result = []
    for i in range(101):
        if answer[i] == 0:
            break
        else:
            result.append(answer[i])
    return result

## 문제 풀이
# - answer을 구하는 과정이 쉽지 않았다.
# - 배포가능 날짜들이 적힌 리스트를 돌면서
# - 앞의 날짜보다 값이 작으면 +1해주고
# - 값이 크면 그 다음 배열에 +1해주는 형식으로 했다.