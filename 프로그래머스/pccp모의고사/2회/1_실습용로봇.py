## 프로그래머스 - pccp 모의고사 2회 1번 - 실습용 로봇
# 30분 소요
def solution(command):
    robot = [0,0]

    view = [0,1] # 로봇이 바라보고 있는 방향 초기값 : 위를 보고있음
    for word in command:
        if word=='G':
            robot[0] += 1*view[0]
            robot[1] += 1*view[1]
        elif word=='B':
            robot[0] -= 1*view[0]
            robot[1] -= 1*view[1]
        elif word=='R':
            a = view[0]
            b = view[1]
            view[0] = b
            view[1] = -a
        elif word=='L':
            a = view[0]
            b = view[1]
            view[0] = -b
            view[1] = a
    return robot

## 문제 풀이
# 로봇이 바라보고 있는 방향을 나타내는 배열 view : 위아래를 바라보고 있다면 움직일 때 x좌표는 안 움직이고 y좌표만 바뀐다. 왼쪽오른쪽을 바라본다면 x좌표만 바뀌고 y좌표는 안 바뀐다
# 전진 혹은 후진할 때 : view에다가 1을 곱한 값만큼 더하거나 빼면 된다.
# 회전할 때 : 오른쪽 회전할 때는 로봇이 보는 방향이 [0,1],[1,0],[0,-1],[-1,0] 이렇게 움직인다.
# x좌표의 변화를 살펴보면 0 1 0 -1 이고, y좌표 변화는 1 0 -1 0 이다. a상태에서 b상태로 바뀔 때 b상태의 x좌표는 a상태의 y값이고, b상태의 y좌표는 a상태의 -x값이 된다.
# 반대로 왼쪽 회전할 때는 x좌표에 -가 붙는다.