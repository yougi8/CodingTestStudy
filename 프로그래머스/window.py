## 프로그래머스 연습문제 - 바탕화면 정리 (99클럽 미들러 문제) level 1

import sys
def solution(wallpaper):
    answer = []
    ## 최소한의 이동거리
    ## 가장 위, 가장 왼, 가장 오, 가장 아래의 파일을 찾아서 각각 점 하나씩만 가져가면 되나?

    ## 세로길이 n / 가로 길이 m
    n = len(wallpaper)

    m = len(wallpaper[0])
    lux, luy, rdx, rdy = -1, -1, -1, -1
    # 시작점 찾기 - 가장 위쪽의 행값(첫번째), 가장 왼쪽의 열값(두번째)
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                lux = i
                break
        if lux != -1:
            break
    for i in range(m):
        for j in range(n):
            if wallpaper[j][i] == "#":
                luy = i
                break
        if luy != -1:
            break
            # 끝점 찾기 - 가장 아래쪽의 행값(첫번째), 가장 오른쪽의 열값(두번째)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if wallpaper[i][j] == "#":
                rdx = i + 1
                break
        if rdx != -1:
            break
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if wallpaper[j][i] == "#":
                rdy = i + 1
                break
        if rdy != -1:
            break
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)

    return answer

wallpaper = list(map(str, sys.stdin.readline().split()))
print(solution(wallpaper))

### 문제 풀이
# - 바탕화면의 크기 nxm (n은 wallpaper의 길이, m은 wallpaper 하나하나 각각의 길이)
# - 시작점 : 가장 위쪽의 행값 + 가장 왼쪽의 열값
# - 끝점 : 가장 아래쪽의 행값 + 가장 오른쪽의 열값

# - for문 4번 돌아서, 시작점의 x,y값, 끝점의 x,y값을 찾아줬다.
# - 시작점의 x,y → i,j값 그대로 사용
# - 끝점의 x,y → 칸의 오른쪽값을 사용하는 것이기 때문에 i,j에 1씩 더해서 사용
# - 끝점 구할 때는 가장 오른쪽, 가장 아래쪽의 값을 가져와야하기 때문에 for문을 앞에서부터 돌지 않고 끝에부터 돌았다.
#   근데 이때 끝나는 인덱스를 0으로 해서 테스트케이스 한개가 계속 통과되지 않았다!
#   끝나는 인덱스를 0으로 하면 0이 포함되지 않으니까 1해서 하기
# - 아쉬운점
#     - `answer.append()` 이 부분을 4번이나 썼어야 했을까?