## 프로그래머스 pccp 모의고사 1회 3번 - 유전법칙
def search(gen, pos):
    if gen == 1:
        return "Rr"
    parent = search(gen - 1, pos // 4)

    if parent == 'RR':
        return 'RR'
    elif parent == 'rr':
        return 'rr'

    now = pos % 5
    if parent == 'Rr':
        if now == 1:
            return 'RR'
        elif now == 2 or now == 3:
            return 'Rr'
        else:
            return 'rr'


def solution(queries):
    answer = []

    for gen, pos in queries:
        answer.append(search(gen, pos))
    return answer