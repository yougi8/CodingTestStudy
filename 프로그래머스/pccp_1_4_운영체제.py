## pccp 모의고사 1회 4번 - 운영체제
import heapq

def solution(program):
    answer = [0] * 11

    program.sort(key=lambda x: (x[1], x[0]))
    q = []

    now = 0
    idx = 0

    while q or idx < len(program):
        for i in range(idx, len(program)):
            if program[i][1] <= now:
                heapq.heappush(q, (program[i][0], program[i][1], program[i][2]))
                idx += 1
            else:
                break

        if q:
            score, put, run = heapq.heappop(q)
            # print(score,put,run)
            answer[score] += now - put
            now += run
        else:
            # 실행할 프로그램이 q에 들어있지 않다면, 현재 시간을 옮김
            # 1씩 증가시켜줄 필요가 없다
            now = program[idx][1]
    answer[0] = now
    print(answer)

solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]])

## 문제 풀이
# 처음에 : heapq 안쓰고, 리스트를 매번 처음부터 돌면서 실행시킬 프로그램을 찾았다. -> 50% 시간초과
# heapq에 set처럼 추가 가능!