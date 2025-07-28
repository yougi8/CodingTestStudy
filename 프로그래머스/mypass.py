## 2025 프로그래머스 코드챌린지 - 유연근무제 https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    answer = 0

    # 주말 찾기 (제외해야 하니까)
    sat = 5
    sun = 6
    for i, num in enumerate(range(startday, startday + 7)):
        if num % 7 == 6:
            sat = i
        elif num % 7 == 0:
            sun = i

    # 한사람씩 계산
    for k, timelog in enumerate(timelogs):
        # 출근 약속 시간. 허용 +10분. 59분까지 표현 가능한 것을 생각해서 60 넘어가면 hour로 넘기기
        promise = schedules[k] + 10
        if promise % 100 >= 60:
            promise = promise + 100 - 60

        # 5일동안 제대로 출근했는지 카운트
        cnt = 0
        for i, time in enumerate(timelog):
            # 주말제외
            if i == sat or i == sun:
                continue

            # 실제 출근시간과 계획시간의 차이
            real = promise - time
            if real >= 0:
                cnt += 1

        # 5일동안 출근했으면 리워드 인정
        if cnt == 5:
            answer += 1

    return answer