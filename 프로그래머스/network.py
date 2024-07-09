## 프로그래머스 43162 네트워크
def solution(n, computers):
    answer = 0

    def dfs(idx):
        visited[idx] = True
        for i in range(n):
            if i != n and visited[i] == False and computers[idx][i] == 1:
                dfs(i)

        return

    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
    return answer