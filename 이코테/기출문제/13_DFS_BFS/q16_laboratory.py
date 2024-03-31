## 이코테 기출문제 DFS/BFS 16번 - 연구소
## 0은 빈칸, 1은 벽, 2는 바이러스
## 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수
## 빈칸의 개수는 3개 이상
## 벽은 3개를 새로 세워야 한다.
import sys
input = sys.stdin.readline

# 세로 n, 가로 m (3<=n,m<=8)
n, m = map(int, input().split())

## 연구실 지도 값 입력
graph = []
for i in range(n):
        virus = list(map(int, input().split()))
        graph.append(virus)

## 이동방향 왼,오,위,아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

## 벽 설치 후 지도
after = [[0]*m for _ in range(n)]

## 안전구역 면적
result = 0

## 바이러스 전파시키는 함수
def virus(x,y):
    ## 왼, 오, 위, 아래로 살펴보며 전파하기
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 지도 내에 있는지 범위 확인
        if nx>=0 and nx<n and ny>=0 and ny<m:
            # 0이라면 바이러스 심기
            if after[nx][ny] == 0:
                after[nx][ny] = 2
                virus(nx,ny) # 바이러스 심었으니까 다시 전염시키기. 재귀함수 호출

## 안전구역 계산하는 함수
def count():
    sum = 0
    for i in range(n):
        for j in range(m):
            if after[i][j] == 0:
                sum += 1
    return sum


def dfs(wall):
    global result # 안전구역이 몇개인지 카운트할 변수. 함수 밖에서 정의되어서 사용중이다.
    ## 벽 3개 설치 완료되었을 때 - 바이러스 전파하고 계산하기
    if wall == 3:
        for i in range(n):
            for j in range(m):
                # 완료 후 지도에 값 복사하기
                after[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if after[i][j] == 2:
                    virus(i,j) # 바이러스 전파

        ## 현재 result값이랑, 새롭게 얻은 count값 중에서 안전구역 수가 더 많은 것으로 선택
        result = max(result, count())
        return
    ## 벽 세우기
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    wall += 1 # 벽 세웠으니까 카운트 올리기

                    dfs(wall) # 또 벽 세울 곳 찾아보기

                    graph[i][j] = 0 # 벽 세우는 경우의 수를 찾는 것이기 때문에, 세웠던 벽을 제거하면서 새로새로 조합 만들어보기
                    wall -= 1



dfs(0)
print(result)





### input
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2 => 9
### input
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
