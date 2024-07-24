## 프로그래머스 - 혼자놀기의 달인

## result의 길이가 2보다 작은 경우, 런타임 에러 조심하기!
def solution(cards):
    answer = 0
    n = len(cards)
    visited = [0] * n
    result = []

    for i in range(n):
        cards[i] = cards[i] - 1

    def cal(idx, cnt):
        if visited[idx] == 1:
            result.append(cnt)
            return
        cnt += 1
        visited[idx] = 1
        cal(cards[idx], cnt)
        return

    for i in range(n):
        if visited[i] == 0:
            cal(i, 0)

    result.sort(reverse=True)
    if len(result) < 2:
        return 0
    else:
        return result[0] * result[1]