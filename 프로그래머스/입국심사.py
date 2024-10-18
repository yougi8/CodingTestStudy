## 프로그래머스 Lv3 입국심사 - https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 1e9
    ## step1. 심사관들의 심사 시간을 오름차순 정렬
    times.sort()

    ## step2. 입국심사를 기다리는 사람을 기준으로 보는 것이 아니라, 심사관 한 명당 몇 명의 사람을
    ## 담당할 수 있는지 체크 -> 이론상 가능한 최소시간 & 가능한 최대시간 설정
    start = times[0]  # 심사시간이 가장 적게 걸리는 심사관의 시간이 최소
    end = times[-1] * n  # 심사시간이 가장 많이 걸리는 심사관이 모든 사람을 담당할 때가 최대

    ## step3. 주어진 시간별로 각 심사관마다 몇명을 담당하는지 체크. 합한 값이 n과 같을 때까지 시간 수정
    while start <= end:
        total = 0  # 심사관들이 담당하는 사람 수
        mid = (start + end) // 2  # 모든 사람이 심사를 받는 데 걸리는 시간을 가운데값으로 가정

        # 각 심사관별로 주어진 시간동안 처리 가능한 사람의 수
        for time in times:
            total += mid // time

        # 모든 심사관이 담당한 사람의 수가 n보다 크거나 같다면 answer 업데이트
        if total >= n:
            answer = mid
            end = mid - 1  # 더 적은 시간으로 처리 가능할 수도 있으니 시간 범위 줄여주기
        # 주어진 시간 안에 n을 모두 다 심사볼 수 없는 경우는 시간 범위 늘려주기
        else:
            start = mid + 1

    return answer

## 문제 풀이
# 이게 왜 이진탐색인지 잘 모르겠긴 하다.
# n이 너무너무너무 크므로 n을 다 돌면서 체크할 수는 없음!
# 심사 시간을 기준으로 이진탐색 수행