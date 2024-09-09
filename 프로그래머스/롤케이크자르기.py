## 프로그래머스 - Lv.2 롤케이크 자르기 https://school.programmers.co.kr/learn/courses/30/lessons/132265
def solution(topping):
    answer = 0

    # 토핑을 처음에 한명에게 몰빵. 다양성만 체크할 거니까 set으로
    left = set()
    right = set(topping)
    count = {}

    # 토핑이 각 몇개씩 있는지 저장 (오른쪽이 가지고 있는 토핑의 개수가 되겠지)
    for i in topping:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # 토핑을 하나씩 상대에게 넘겨주면서 다양성 체크
    for top in topping:
        left.add(top)  # 왼쪽 토핑 리스트에 한개 줌
        count[top] -= 1  # 토핑개수 저장된 리스트에서 해당 토핑 개수 1개 삭제

        # 만약에 오른쪽이 가지고 있는 토핑의 개수가 0이 된다면 -> 오른쪽은 그 토핑을 안가지고 있는 것.
        # 오른쪽 토핑 셋에서 삭제시켜줘야 함
        if count[top] == 0:
            right.remove(top)
        if len(left) == len(right):
            answer += 1
    return answer

# 시간초과 코드
# def solution(topping):
#     answer = 0
#     for i in range(1,len(topping)):
#         left = set(topping[:i])
#         right = set(topping[i:])
#         if len(left)==len(right):
#             answer += 1

#     return answer