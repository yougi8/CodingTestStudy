## 프로그래머스 - 기지국 설치 Lv3 https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math
def solution(n, stations, w):
    answer = 0

    cover = w * 2 + 1  # 기지국 하나 설치로 커버 가능한 아파트 개수
    start = 1  # 전파 닿는지 확인 할 아파트 시작 번호
    end = 0  # 전파 닿는지 확인 할 아파트 끝 번호
    for station in stations:
        end = station - w  # 해당 기지국 세웠을 때 전파 닿는 젤 왼쪽 아파트
        empty = end - start
        # 전파가 닿지 않는 아파트가 있을 때
        if empty > 0:
            answer += math.ceil(empty / cover)
            # print(start,end,math.ceil(empty/cover))
            start = end + cover
        else:
            start = station + w + 1

    # 마지막 기지국(stations에 있는) 설치 후에 그 뒤에 안 닿는 아파트 처리
    if start <= n:
        answer += math.ceil((n - start + 1) / cover)

    return answer

## 문제 풀이
# 키포인트 : 마지막 기지국 확인할 때 start가 n보다 작은 게 아니라, 작거나 같은 경우까지 봐줘야한다! 즉, 등호가 있어야함



