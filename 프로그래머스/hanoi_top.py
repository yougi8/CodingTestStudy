# 프로그래머스 12946 하노이의 탑
def solution(n):
    answer = []

    def move(now, start, end, mid):
        if now == 1:
            answer.append([start, end])
            return

        move(now-1, start, mid, end)
        answer.append([start,end])
        move(now-1, mid, end, start)
        return

    move(n, 1, 3, 2)
    return answer

print(solution(2))