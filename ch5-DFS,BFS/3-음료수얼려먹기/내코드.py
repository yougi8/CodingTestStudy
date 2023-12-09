# n,m = map(int, input().split())
# graph = []
#
# for i in range(n):
#     graph.append(list(map(int, input())))
n,m = 3, 3
graph = [
    [0,0,1],
    [0,1,0],
    [1,0,1]
]

def dfs(x, y):
    # 범위 설정 꼭 해줄 것
    if x<0 or y<0 or x>=n or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문완료

        # 상하좌우로 dfs 실행!
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

