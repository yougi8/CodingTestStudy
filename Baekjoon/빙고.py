## 백준 실버4 빙고
import sys
input = sys.stdin.readline

bingo = []
for i in range(5):
    bingo.append(list(map(int,input().split())))

target = []
for i in range(5):
    target.extend(list(map(int, input().split())))

def find(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                return

def check():
    total = 0
    # 가로 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt += 1
            else:
                break
        if cnt == 5:
            total += 1

    # 세로 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt += 1
            else:
                break
        if cnt == 5:
            total += 1

    # 우하향 대각선 확인
    cnt = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt += 1
    if cnt == 5:
        total += 1

    # 우상향 대각선 확인
    cnt = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        total += 1

    if total >= 3:
        return True

    else:
        return False

for i, number in enumerate(target):
    find(number)
    if i>=11 and check() == True:
        print(i+1)
        break


## input
# 11 12 2 24 10
# 16 1 13 3 25
# 6 20 5 21 17
# 19 4 8 14 9
# 22 15 7 23 18
# 5 10 7 16 2
# 4 22 8 17 13
# 3 18 1 6 25
# 12 19 23 14 21
# 11 24 9 20 15
## output
# 15

## 문제 풀이
# 3빙고가 될 수 있는 숫자의 최소 수를 13개라고 생각해서 자꾸 오답이 나왔다.
# 그치만 최소 수는 12개이므로 마지막 for문을 돌 때 조건문에서 i>=11로 해야 정답이다! (i가 0부터 시작하기 때문)