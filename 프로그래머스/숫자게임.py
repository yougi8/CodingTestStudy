## 프로그래머스 숫자게임 Lv3. https://school.programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    idx = 0
    for a in A:
        if a >= B[idx]:
            continue
        else:
            idx += 1
            answer += 1
    return answer

## 문제 풀이
# 처음에는 그냥 오름차순 정렬로 하고, 각 값마다 비교를 했는데 예제케이스는 통과하지만 답은 아니었다!
# 내림차순으로 정렬하고, A는 순서대로 비교하고 B는 통과된? 애들만 비교한다
# 처음에 idx = 0으로 설정하고, A랑 비교했을 때 더 큰 값이면 그 다음 B를 비교할 수 있게 된다