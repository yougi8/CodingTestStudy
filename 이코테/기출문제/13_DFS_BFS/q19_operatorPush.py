# 이코테 기출문제 dfs/bfs - 19. 연산자 끼워 넣기(삼성sw역량테스트, 백준 14888)
import sys
input = sys.stdin.readline

n = int(input()) # 2<=n<=11
number = list(map(int, input().split())) # 숫자 종류? 배열
oper = list(map(int, input().split())) # 연산자 등장 횟수 - 덧셈+ 뺄셈- 곱셈* 나눗셈/

maxValue = -1e9
minValue = 1e9

def dfs(i, answer):
    global maxValue, minValue
    if i == n:
        maxValue = max(maxValue, answer)
        minValue = min(minValue, answer)
        return
    else:
        if oper[0]>=1:
            oper[0] -= 1
            dfs(i+1, answer+number[i])
            oper[0] += 1
        if oper[1]>=1:
            oper[1] -= 1
            dfs(i+1, answer - number[i])
            oper[1] += 1
        if oper[2]>=1:
            oper[2] -= 1
            dfs(i+1, answer * number[i])
            oper[2] += 1
        if oper[3] >= 1:
            oper[3] -= 1
            dfs(i+1, int(answer/number[i]))
            oper[3] += 1

dfs(1,number[0])

print(int(maxValue))
print(int(minValue))


## 문제 풀이
# 도대체 왜 경우의 수 한가지만 도는거지? 그니까 맨 처음 계산한 경우만 끝내고 바로 리턴을 해버림..
# 그래서 각 예시마다 첫 번째 값인 30, 35, 1이 max랑 min에 모두 들어가게됨
# 하지만 난 경우의 수를 모조리 다 계산해야된다는거죠..?

# 예시2번으로 해보자면, 연산 두개 다 썼을 때 else 문에서 끝나버림! 움... 하지만 다시 시작해야되는데..
# 연산자 판단하는 부분을 if-elif로 묶는 게아니라!!!! if if if 로 해야지 재귀가 끝나고 돌아와도 또! 탐색해볼 수 있음..

## 틀렸습니다
# 백준에서 47%? 쯤에서 틀림. 히든케이스겠지?
# int() 씌우면 걍 양수로 나오는 줄 알았는데, 아니었음. 음수로 나오네 왜지
# print(int(10/3)) -> 3
# print(int(-10/3)) -> -3
# 아니다 생각해보면 애초에 양수로 바꿀 필요가 없다.. 왜냐면 그런 조건은 없었으니까..
# ==> 바로바로 1e9가 당첨되어서 float값으로 나오는 경우였습니다!! Hㅏ... 출력할 때 int 씌워주기..