## 프로그래머스 - 연속 펄스 부분수열의 합
def solution(sequence):
    N = len(sequence)
    if N == 1:
        return max(sequence[0], -sequence[0])

    first = [0] * N # 1 -1 1 -1 ... 값을 저장할 배열
    second = [0] * N # -1 1 -1 1 ... 값을 저장할 배열
    for i in range(0, N, 2):
        first[i] = sequence[i]
        second[i] = -sequence[i]
        if i == N - 1 and i % 2 == 0:
            continue
        first[i + 1] = -sequence[i + 1]
        second[i + 1] = sequence[i + 1]

    dp_f = [0] * N
    dp_s = [0] * N
    dp_f[0] = first[0]
    dp_s[0] = second[0]

    # 부분합 구하기 : 현재 시점에서 나만 가지고 가는게 더 큰지, 앞에 있는 부분합까지 가져가는게 더 큰지 판단
    for i in range(1, N):
        dp_f[i] = max(first[i], first[i] + dp_f[i - 1])
        dp_s[i] = max(second[i], second[i] + dp_s[i - 1])
    return max(max(dp_f), max(dp_s))
solution([2, 3, -6, 1, 3, -1, 2, 4])

## 문제풀이
# 처음에는 dp 사용 안하고 풀었는데, 절반이 시간초과
# 누적합 & 부분합은 dp를 사용해야한다
# 부분합 : 현재를 기준으로 이전 누적합(=부분합)을 포함시키는게 유리한지 아닌지 판단. 바로 이전 dp값만 판단하면 된다

## 복습 후 코드 개선 (dp배열 따로 안 만들기)
def solution(sequence):
    ## step1. 펄스 수열 만들기
    positive = []  # 1 -1 1 -1 배열
    negative = []  # -1 1 -1 1 배열

    flag = 1
    for num in sequence:
        positive.append(num * flag)
        flag *= -1
        negative.append(num * flag)

        ## step2. 부분합 찾기
    n = len(sequence)

    # 현재 내 값 vs 내 값 + 앞의 값 합산  // 중에서 더 큰 값으로 업데이트하기 (dp)
    for i in range(1, n):
        positive[i] = max(positive[i - 1] + positive[i], positive[i])
        negative[i] = max(negative[i - 1] + negative[i], negative[i])

    return max(max(positive), max(negative))

