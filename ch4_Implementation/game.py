## 이코테 p.118 게임개발
import sys
def turn_left(direction):
    # 북쪽 direction 번호가 0 이니까, 북쪽에서 왼쪽 회전하면 서쪽이니까 direction 3으로 설정해주기
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    return direction

def move(x, y, direction, maps):
    total = 0
    ## 방문 기록하는 배열
    visited = [[0] * n for _ in range(m)]
    visited[x][y] = 1  # 시작 위치는 방문처리

    # 북:0, 동:1, 남:2, 서:3 니까 순서를 이렇게 부여
    dx = [-1, 0, 1, 0]  ## 북동남서
    dy = [0, 1, 0, -1]  ## 북동남서

    temp = 0 # 회전하는 횟수 저장(방향이 다시 제자리로 돌아왔는지 체크)

    ## 더이상 갈 곳이 없을 때(네 방향이 모두 가본 곳이거나 바다여서 못갈 때, 뒤쪽방향까지 바다인 상황)까지 게임 진행
    while(True):
        direction = turn_left(direction)
        temp += 1

        nx, ny = x + dx[direction], y + dy[direction]
        ## 전진할 곳이 이미 방문한 곳일 때 : 다시 turn함
        if temp!= 4 and visited[nx][ny] == 1:
            continue
        ## 전진할 곳이 육지이면서 방문한 곳이 아닐 때
        elif temp != 4 and maps[nx][ny] == 0:
            x, y = nx, ny
            visited[x][y] = 1
            print('전진!')
            temp = 0
            total += 1
        ## 전진할 곳이 바다일 때
        else:
            nx2, ny2 = x+dx[direction-2], y+dy[direction-2]
            ## 방향이 다시 제자리로 왔는데 뒤로가면 바다인 경우 -> 종료
            if temp == 4:
                if maps[nx2][ny2] == 1:
                    break
                else:
                    print('백!')
                    temp = 0
                    total += 1
                    x, y = nx2, ny2
            ## 제자리로 안 왔으면 다시 회전하기
            else:
                continue

    print('움직인 횟수 : ', total)


n, m = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())
maps = [] # 지도
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

move(x, y, direction, maps)


