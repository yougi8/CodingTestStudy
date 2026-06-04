## 프로그래머스 Lv.2 구명보트 - https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    
    ## 오름차순 정렬
    people.sort()
    
    light = 0 # 하나는 최소부터 증가
    heavy = len(people)-1 # 하나틑 최대부터 감소
    
    while light<=heavy:
        # 최소 + 최대 더했을 때 limit을 넘지 않으면 -> 같이 태워서 보냄
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
        
        # limit을 넘으면 -> 최대만 태워서 보냄
        else:
            heavy -= 1
        
        answer += 1
    
        
    return answer

## "최대 2명만 매칭 가능", "무게나 크기 제한 존재", "최소/최대 개수 구하기"
## -> 정렬 후 양끝을 비교하는 그리디+투 포인터