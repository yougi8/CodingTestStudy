import sys
n = int(sys.stdin.readline())
plans = sys.stdin.readline().split()

x, y = 1, 1 # 시작 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R'] # 상하좌우

# 이동 계획을 하나씩 확인
for i in plans:
    # 이동 후 좌표 구하기
    for j in range(len(move_types)):
        if i == move_types[j]:
            new_x = x + dx[j]
            new_y = y + dy[j]
    # 공간을 벗어나는 경우 무시
    if new_x<=0 or new_x>n or new_y<=0 or new_y>n:
        continue
    # 공간 벗어나지 않는다면 이동 수행
    x = new_x
    y = new_y

print(x, y)



