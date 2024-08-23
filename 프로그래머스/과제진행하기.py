## 프로그래머스 - 과제 진행하기 Lv2 https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    answer = []
    wait = [] # 대기중인 과제들
    for plan in plans:
        time = int(plan[1][0:2]) * 60 + int(plan[1][3:5])
        plan[1] = time
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])
    # print(plans)

    for i in range(len(plans) - 1):
        wait.append(plans[i])
        remain = plans[i + 1][1] - plans[i][1]  # 다음 과제가 들어오기까지 주어진 시간 (과제 수행할 수 있는 시간)

        while wait and remain:
            work = wait[-1][2]  # 현재 진행 할 과제의 걸리는 시간

            if work <= remain:  # 현재 과제가 다음 과제 전에 끝난다면
                subject, start, do = wait.pop()
                remain -= do # 현재 과제 처리하고 또 남은 시간에 대기열에 있는 과제를 처리할 수도 있기 때문에 remain 업데이트해줌
                answer.append(subject)
            else:
                wait[-1][2] -= remain # 과제 진행한만큼 남은시간 업데이트 해주기
                work -= remain
                break # 다 못했다는 것은, 다음 과제가 들어와야한다는 뜻이기 때문에 while문 나가서 다음 들어오는 과제를 수행한다

    answer.append(plans[-1][0]) # 마지막 과제는 위의 for문으로 추가가 안됐으니 마지막에 한번 추가해주기

    # 끝마치지 못한 과제 대기열에 들어가있는 애들은 더이상 다음 과제 들어오는 시간과 상관없이 처리하면 된다. 뒤에부터 answer에 추가해준다
    for i in range(len(wait) - 1, -1, -1):
        answer.append(wait[i][0])

    return answer

## 문제 풀이
# while문 안에 else에는 과제를 하다가 다 못 마치고 다른 과제가 들어오는 경우인데, 이 경우에는 과제를 조금이라도 했으니까 과제 걸리는 시간을 빼서 업데이트 해줘야한다!
# → 즉, 60짜리 과제를 10만큼 하고 넘어갔으면 이제 그 과제의 남은 시간은 50이 되니까 50으로 업데이트 해줘야 한다 `wait[-1][2]` 이 코드 안쳐서 정답률 58%였다 계속