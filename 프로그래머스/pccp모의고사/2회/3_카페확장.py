## 프로그래머스 pccp 모의고사 2회 3번 - 카페확장
def solution(menu, order, k):
    answer = 0
    q = []  # 현재 대기중인 음료의 남은 제조시간. 각 손님이 도착할 때마다 그 손님 음료를 만드는 데 걸리는 시간을 저장
    answer = []  # 처음에는 매번 max값으로 answer을 업데이트 했는데, 그러면 시간복잡도가 더 커짐. 그럴 필요 x 마지막에 한번만 찾자

    for drink in order:
        q.append(menu[drink])
        answer.append(len(q))

        # q[0]은, 현재 만들고 있는 음료로. 음료를 완성하는 데까지 얼만큼의 시간이 남았는지 저장
        # 즉, 새로운 손님이 도착할 때마다 현재 제조중인 음료가 얼마나 더 만들어졌는지 저장하는 것
        q[0] -= k

        while q and q[0] <= 0:
            # 지금 만들고 있는 음료가 완성되는 데까지 걸리는 시간이 저장된 q[0]이 음수라면
            # 이미 다 만들어진 것! 그렇다면 해당 음료를 대기열에서 빼줘야 한다.
            if q[0] <= 0:
                # 첫번째 음료가 다 만들어진 상태일 때, 두 번째 음료가 대기중이었다면
                if len(q) >= 2:
                    # 첫 번째 음료가 초과된 시간 동안 완성된 경우 그 시간을 다음 음료 제조 시간에 반영
                    q[1] += q[0]
                q.pop(0)
    return max(answer)