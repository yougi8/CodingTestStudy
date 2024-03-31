import sys
## 얼음 틀 사이즈 입력받기
n, m = map(int, sys.stdin.readline().split())

## 얼음틀 배열 생성 & 입력받기
ice = []
for i in range(n):
    ice.append(list(map(int, input()))) ## 원래는 sys 사용하는데, 그렇게 하면 0이 없는 값 처리가 되어서.. 걍 input() 사용함

icecream = 0 # 아이스크림 개수
dx = [-1 ,1, 0, 0]# 상하좌우
dy = [0, 0, -1, 1]# 상하좌우
def dfs(x,y):
    ## 주어진 범위 밖으로 벗어날 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 아직 탐색하지 않은 노드라면(얼음을 얼리기 전이라면) 상하좌우로 탐색하기
    if ice[x][y] == 0:
        ice[x][y] = 1 # 방문처리 하고
        # 상하좌우 방문했는지 살피고 오기!
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

# 참고로 visited 배열은 따로 필요없다. 왜냐면 애초에 얼음틀 배열이 0과 1로 이루어져있기 때문이고, 벽은 방문할 필요가 없으니까
for i in range(n):
    for j in range(m):
        if dfs(i,j): # True로 반환값이 오면 아이스크림 생성 완료!
            icecream += 1
print(icecream)



