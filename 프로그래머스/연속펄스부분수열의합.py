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

