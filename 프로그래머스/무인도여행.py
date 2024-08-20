## 프로그래머스 - 무인도 여행 https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        result = int(maps[x][y])
        visited[x][y] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and visited[nx][ny] != True:
                        result += int(maps[nx][ny])
                        q.append((nx, ny))
                        visited[nx][ny] = True
        return result

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] != True:
                result = bfs(i, j)
                if result != -1:
                    answer.append(result)

    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer

## 문제 풀이
# maps가 ["X591X","X1X5X","X231X", "1XXX1"] 이런식으로 주어져서 나는 이차원 배열을 따로 for문 돌아서 새로 만들었는데
# 이미 이차원 배열이어서 maps[0][0] 이런식으로 사용이 가능하다. 이부분 수정완료
# 마지막에 else return answer.sort() 이렇게 했는데 answer.sort()의 결과값은 null이다!
# sort를 하고 return 해주기