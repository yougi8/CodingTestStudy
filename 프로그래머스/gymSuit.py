import sys


def solution(n, lost, reserve):
    answer = 0

    # 처음엔 체육복이 모두가 있다고 가정
    clothes = [1] * (n + 1)

    # 도난당한 학생은 체육복 정보 0으로 해주기
    for i in range(1, n + 1):
        if i in lost:
            clothes[i] = 0

    # 체육복 빌려주기
    reserve.sort()
    for i in range(len(reserve)):
        if clothes[reserve[i]] == 0:
            clothes[reserve[i]] = 1
        elif clothes[reserve[i] - 1] == 0:
            clothes[reserve[i] - 1] = 1
        elif reserve[i] + 1 <= n and clothes[reserve[i] + 1] == 0 and reserve[i] + 1 not in reserve:
            clothes[reserve[i] + 1] = 1

    answer = clothes.count(1) - 1 # 0번째 학생은 제외

    return answer
print(solution(5, [2,4], [3]))

### 풀이과정
# 테스트 케이스 5번, 12번이 통과가 안됐다.
# 해당 케이스는, 체육복을 잃어버렸지만 여벌이 있는 학생에게, 앞사람이 본인의 체육복을 빌려주려 할 떄다
# 이 경우에는 잃어버린 본인 옷을 입으면 되기 때문에 앞에서 빌려입을 필요가 없다!
# 마지막 elif 구문에서 reserve[i] + 1 not in reserve 이 부분을 추가하여
# 뒤에 빌려줄 학생이 체육복을 잃어버렸지만 여벌을 가지고있진 않은지 확인하면 된다.
# ㅠㅠ 이거 때문에 오래걸렸다 ㅠㅠ