## 프로그래머스 Lv.2 - 연속 부분 수열 합의 개수 https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    n = len(elements)
    double_elements = elements * 2 # 원형큐, 길이 2배로 늘리기
    answer = set() # 중복제거 위해 set 사용
    
    # 시작점 고정하고, 그 시작점에서 길이 1 ~ n 까지 더할 것임
    for start in range(n):
        for length in range(n):
            unique_sum = sum(double_elements[start:start+length])
            answer.add(unique_sum)
                
    return len(answer)


## 원형 배열이나 구조 -> 배열을 늘려주는 기법(elements * 2)이나
## 인덱스를 배열 길이로 나눈 나머지(index % n) 활용