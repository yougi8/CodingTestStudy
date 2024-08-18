## 프로그래머스 lv2. - 마법의 엘리베이터 https://school.programmers.co.kr/learn/courses/30/lessons/148653
import sys
def solution(storey):
    answer = 0

    while storey > 0:
        one = storey % 10
        storey //= 10

        # 일의자리가 5보다 크면
        if one > 5:
            answer += 10 - one  # 올라가기
            storey += 1  # 앞자리 1 더해주기
        # 일의자리가 5보다 작으면
        elif one < 5:
            answer += one  # 내려가기
        # 일의자리가 5이면
        else:
            if storey % 10 >= 5:
                answer += 10 - one
                storey += 1
            else:
                answer += one
    return answer

storey = int(sys.stdin.readline())
print(solution(storey))

### 문제 풀이
## 일의 자리 수가 5보다 작으면 -> 1,2,3,4면 -> 올라가기
## 일의 자리 수가 5보다 크면 -> 6,7,8,9 -> 올라가기 & 앞자리 숫자 1 올려주기
## 일의 자리 수가 5면 -> 앞자리가 5이상이면 올라가는것이 유리.

# - 그리디로 생각
#     - storey를 나누면서, 매번 일의자리,십의자리 숫자만 체크했다.
#     - 일의자리수가 5보다 크면 +1을 하는 것이 유리. → 십의자리수도 1 증가시켜줘야한다.
#     - 일의자리수가 5보다 작으면 -1을 하는 것이 유리
#     - 일의자리수가 5면, 십의자리수가 5이상일 땐 올라가고, 5보다 작을 땐 내려가는 게 유리.
#     - 괜찮게 진행했는데, while문을 도는 조건인 storey를 while문 마지막에 나누기를 하는바람에 답이 살짝 이상하게 나오긴 했다.
#     - 그렇지만 첫 번째 코드에서는 몇몇 테스트케이스를 통과하지 못했다.
#
# - 문제점이 뭐였냐
#     - 일의자리가 5일 경우, 앞자리가 5이상일 때는 올라가는 것이 유리하다.
#     - 이를 처리하는 조건문   `if storey//10 >=5:` 이 부분이 잘못되었다.
#     - 앞자리를 구하려면 // 를 사용해서 몫을 구하는게 아니라, %을 사용해서 나머지를 구해야 했던 것이다!!!!

# ++ dfs로도 풀 수 있을 것 같다.