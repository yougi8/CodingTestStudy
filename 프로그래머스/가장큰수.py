## 프로그래머스 가장 큰 수 Lv2. https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    # 모든 원소가 0일 경우에는 '0'을 정답으로 제출
    if all(n == 0 for n in numbers):
        return "0"

    numbers = list(map(str, numbers))

    # 그냥 내림차순 정렬을 하면 34,30,3이 된다.
    # 이를 방지하기 위해 주어진 값을 3번 반복한 값으로 내림차순 정렬한다.
    # 최대 3자리니까 1자리인 수도 3자리로 맞추려고 3번 반복)
    # -> 343434, 333, 303030 처럼 의도한대로 정렬이 가능
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)

    return answer

## 문제 풀이
# 포인트1. 최대로 주어지는 값이 1000 아니면 세자리 수니까 모든 수를 세자리 이상으로 맞춘 후에 비교하면 원하는대로 내림차순이 가능!
# 3이 30보다 큰 값으로 여겨지니까 세번 반복하면 333이랑 303030을 비교하게 된다. (문자열 비교)
# 포인트2. 모든 원소가 0일 경우에는 원래 문자열 비교를 했으니까 000, 00 이런 식으로 나오게 되는데! 이를 방지하기 위해서
# 모든 원소가 0인 경우에는 '0'으로 리턴하게 조건 미리 걸어두기