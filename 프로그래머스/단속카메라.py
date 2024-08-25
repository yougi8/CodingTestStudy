## 프로그래머스 - 단속카메라 https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1]) # 차량이 나가는 시점을 기준으로 오름차순

    camera = -30001 # 카메라 설치 위치 (초기값 : 도로의 시작지점이 -30,000보다 작은 값
    for route in routes:
        start,end = route[0], route[1]

        # 차량이 들어가는 진입지점이 카메라 설치 위치보다 오른쪽에 있으면 그 카메라에 안 걸리는 것
        if camera < start:
            # 그러면 그 차량이 나가는 지점에다가 카메라를 설치해준다
            answer += 1
            camera = end
    return answer