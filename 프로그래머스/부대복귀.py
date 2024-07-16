## 프로그래머스 부대복귀
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    visited = [-1]*(n+1)
    arr = [[] * (n+1) for _ in range(n+1)]
    for a, b in roads:
        arr[a].append(b)
        arr[b].append(a)

    visited[destination] = 0
    print('arr:',arr)
    def bfs(n):
        queue = deque()
        queue.append(n)

        while queue:
            now = queue.popleft()
            print('now:',now)
            print('visited:',visited)

            for i in arr[now]:
                if visited[i] == -1:
                    visited[i] = visited[now] + 1
                    queue.append(i)
        return

    bfs(destination)

    for i in sources:
        answer.append(visited[i])
    print('visited:',visited)
    print('answer:',answer)
    # return answer

solution(3,	[[1, 2], [2, 3]]	,[2, 3],1)