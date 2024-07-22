## 프로그래머스 땅따먹기
def solution(land):
    answer = 0
    n = len(land)

    for i in range(1, n):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if j == k: continue
                max_value = max(max_value, land[i - 1][k])
            land[i][j] += max_value
    # print(land)

    return max(land[n - 1])