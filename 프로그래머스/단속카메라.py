## 프로그래머스 - 단속카메라 https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    print(routes)
    camera = -30001
    for route in routes:
        start,end = route[0], route[1]
        if camera < start:
            answer += 1
            camera = end
    return answer