from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    count = 0  # 타겟 넘버를 만드는 방법의 수
    while queue:
        # 현재 합계, 인덱스
        current_sum, idx = queue.popleft()

        # 모든 숫자를 다 사용한 경우
        if idx == len(numbers): ## 범위 벗어났을 경우
            # 현재 합계가 타겟과 일치하면 카운트를 1 증가
            if current_sum == target:
                count += 1
        else:
            # 현재 숫자를 더하거나 뺀 경우를 모두 고려하여 큐에 추가
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))

    return count

print(solution([1, 1, 1, 1, 1], 3))

#######################
# 1번쨰 생각
# def solution(numbers, target):
#     count = 0
#     queue = deque([])
#
#     while queue:
#
#         v = queue.popleft()
#         if v == target:
#             count += 1
#
#         for i in range(len(numbers)):
#             queue.append(v + numbers[i])
#             queue.append(v - numbers[i])
#
#     return count