## 프로그래머스 n-queen 12952
def solution(n):
    answer = 0
    graph = [[0] * n for _ in range(n)]
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    def queen(x, y, cnt, answer):
        if cnt == n:
            answer += 1
            cnt = 0
            return

        # 퀸 놓기
        graph[x][y] = 1

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1:
                    graph[x][y] = 0
                    return
                queen(nx, ny, cnt+1, answer)

        return
    queen(0, 0, 0, answer)

    return answer

print(solution(4))